package ar.edu.itba.mna;

import de.erichseifert.gral.data.DataTable;
import de.erichseifert.gral.plots.Plot;
import de.erichseifert.gral.plots.XYPlot;
import org.apache.commons.math3.complex.Complex;
import org.apache.commons.math3.transform.DftNormalization;
import org.apache.commons.math3.transform.FastFourierTransformer;
import org.apache.commons.math3.transform.TransformType;
import org.apache.log4j.BasicConfigurator;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;
import org.jfree.ui.RefineryUtilities;
import org.nd4j.linalg.api.complex.IComplexNDArray;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.cpu.nativecpu.complex.ComplexDouble;
import org.nd4j.linalg.factory.Nd4j;
import org.nd4j.linalg.fft.FFTInstance;
import org.nd4j.linalg.indexing.NDArrayIndex;
import org.opencv.core.*;
import org.opencv.videoio.VideoCapture;
import org.opencv.videoio.Videoio;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.nd4j.linalg.ops.transforms.Transforms;

import java.awt.*;
import java.util.Arrays;

import static org.nd4j.linalg.util.MathUtils.log2;

/**
 * java heartrate implementation
 *
 */
public class Heartrate
{
    private static Logger logger = LoggerFactory.getLogger(Heartrate.class);
    static {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        System.loadLibrary("opencv_ffmpeg330_64");
    }



    public static void main( String[] args )
    {
        BasicConfigurator.configure();
        logger.debug(System.getProperty("user.dir"));
        VideoCapture videoCapture = new VideoCapture("video.mp4");
        int length = (int) videoCapture.get(Videoio.CAP_PROP_FRAME_COUNT);
        int width = (int) videoCapture.get(Videoio.CAP_PROP_FRAME_WIDTH);
        int height = (int) videoCapture.get(Videoio.CAP_PROP_FRAME_HEIGHT);
        int fps = (int) videoCapture.get(Videoio.CAP_PROP_FPS);
        logger.debug("length: {}, width: {}, height: {}, fps: {}", length, width, height, fps);

        INDArray r = Nd4j.zeros(length);
        INDArray g = Nd4j.zeros(length);
        INDArray b = Nd4j.zeros(length);

        for (int i = 0; i < length && videoCapture.isOpened(); i++) {
            Mat mat = new MatOfInt(width, height);

            if (videoCapture.read(mat)) {
                Scalar means = Core.mean(mat.submat(new Range(625, 655), new Range(345, 375)));
                r.put(0, i, means.val[0]);
                g.put(0, i, means.val[1]);
                b.put(0, i, means.val[2]);
            }
        }
        videoCapture.release();

        int n = (int)Math.pow(2, Math.floor(log2(length)));
        logger.debug("n: {}", n);
        r = r.get(NDArrayIndex.interval(0, n));
        g = g.get(NDArrayIndex.interval(0, n));
        b = b.get(NDArrayIndex.interval(0, n));
        r = r.subi(r.meanNumber());
        g = g.subi(g.meanNumber());
        b = b.subi(b.meanNumber());

        double [] rarr = Arrays.copyOfRange(r.data().asDouble(), 0, n);
        double [] garr = Arrays.copyOfRange(g.data().asDouble(), 0, n);
        double [] barr = Arrays.copyOfRange(b.data().asDouble(), 0, n);

        long start = System.currentTimeMillis();

//        FastFourierTransformer fft = new FastFourierTransformer(DftNormalization.STANDARD);
//        Complex[] R = fft.transform(rarr, TransformType.FORWARD);
//        FFT.fftshift(R);
//        double[] Rsq = FFT.complexSquare(R);
//        Complex[] G = fft.transform(garr, TransformType.FORWARD);
//        FFT.fftshift(G);
//        double[] Gsq = FFT.complexSquare(G);
//        Complex[] B = fft.transform(barr, TransformType.FORWARD);
//        FFT.fftshift(B);
//        double[] Bsq = FFT.complexSquare(B);

        Complex[] R = FFT.fft(rarr);
        FFT.fftshift(R);
        double[] Rsq = FFT.complexSquare(R);
        Complex[] G = FFT.fft(garr);
        FFT.fftshift(G);
        double[] Gsq = FFT.complexSquare(G);
        Complex[] B = FFT.fft(barr);
        FFT.fftshift(B);
        double[] Bsq = FFT.complexSquare(B);
        long end = System.currentTimeMillis();

        g = Nd4j.getNDArrayFactory().create(Gsq);

        INDArray arg = Nd4j.argMax(g);
        INDArray f = Nd4j.linspace(-n / (double) 2, n / (double) 2 - 1, n).mul(fps / (double) n);
        logger.debug("fft time: {}", end - start);
        logger.debug("fft: {} ", Rsq);
//        f[np.argmax(G)]) * 60
        ;
        logger.debug("Frecuencia cardiaca {}", f.getDouble((int)arg.getDouble(0) > n / 2 ? (int)arg.getDouble(0) : n  - (int)arg.getDouble(0)) * 60);

//        logger.debug("frecuencia: {}", farr[(int)] * 60);
        XYChart chart = new XYChart(
                "stats",
                "stats",
                buildDataset(Rsq, Gsq, Bsq),
                buildRenderer()
        );
        chart.pack();

        RefineryUtilities.centerFrameOnScreen(chart);
        chart.setVisible(true);
//        Plot plot = new XYPlot()

    }

    private static XYDataset buildDataset(double[] R, double[] G, double[] B) {
        final XYSeries rseries = new XYSeries("Red");
        for (int i= R.length / 2; i < R.length/2 + 200; i++) {
            rseries.add(i, R[i]);
        }
        final XYSeries gseries = new XYSeries("Green");
        for (int i=G.length / 2; i < G.length/2 + 200; i++) {
            gseries.add(i, G[i]);
        }
        final XYSeries bseries = new XYSeries("Blue");
        for (int i=B.length/2; i < B.length/2 + 200; i++) {
            bseries.add(i, B[i]);
        }
        final XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(rseries);
        dataset.addSeries(gseries);
        dataset.addSeries(bseries);
        return dataset;
    }

    private static XYLineAndShapeRenderer buildRenderer() {
        XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer( );
        renderer.setSeriesPaint( 0 , Color.RED );
        renderer.setSeriesPaint( 1 , Color.GREEN );
        renderer.setSeriesPaint( 2 , Color.BLUE );
        renderer.setSeriesStroke( 0 , new BasicStroke( 0.1f ) );
        renderer.setSeriesStroke( 1 , new BasicStroke( 0.1f ) );
        renderer.setSeriesStroke( 2 , new BasicStroke( 0.1f ) );
        return renderer;
    }
}
