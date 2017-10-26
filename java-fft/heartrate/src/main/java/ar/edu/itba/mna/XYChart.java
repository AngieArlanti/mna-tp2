package ar.edu.itba.mna;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.xy.XYDataset;
import org.jfree.ui.ApplicationFrame;

/**
 * Created by santiago on 21/10/2017.
 */
public class XYChart extends ApplicationFrame {

    public XYChart(String applicationTitle,
                   String chartTitle,
                   XYDataset dataset,
                   XYLineAndShapeRenderer renderer) {
        super(applicationTitle);
        JFreeChart xylineChart = ChartFactory.createXYLineChart(
                chartTitle ,
                "Category" ,
                "Score" ,
                dataset,
                PlotOrientation.VERTICAL ,
                true , true , false);
        ChartPanel chartPanel = new ChartPanel( xylineChart );
        chartPanel.setPreferredSize( new java.awt.Dimension( 560 , 367 ) );
        setContentPane(chartPanel);
    }
}
