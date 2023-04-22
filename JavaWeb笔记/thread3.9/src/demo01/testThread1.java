package demo01;

//多线程下载图片，线程的执行顺序完全由cpu调度决定

import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.net.URL;

import static org.apache.commons.io.FileUtils.*;

public class testThread1 extends Thread{
    private String url;
    private  String name;

    public testThread1(String url, String name) {
        this.url = url;
        this.name = name;
    }

    @Override
    public void run() {
        WebDownloader webdownloader = new WebDownloader();
        webdownloader.Download(this.url , this.name);
        System.out.println("下载了图片："+name);

//        super.run();
    }

    public static void main(String[] args) {
        testThread1 myThread1 = new testThread1("https://i0.hdslb.com/bfs/sycp/creative_img/202110/e04c7beb12c779dfe30730a9a8b2f0fe.jpg@.webp" , "图片1.webp");
        testThread1 myThread2 = new testThread1("https://i2.hdslb.com/bfs/face/83bb511365da513c55aa3d1958524f3b7db40684.jpg@120w_120h_1c_1s.webp" , "图片2.webp");
        testThread1 myThread3 = new testThread1("https://i2.hdslb.com/bfs/face/b8040c9b600b72f1564c299f2d0405c410359a59.jpg@240w_240h_1c_1s.webp" , "图片3.webp");

        myThread1.start();
        myThread2.start();
        myThread3.start();

    }
}

class WebDownloader{

    public void Download(String url , String fname) {
        try {
            copyURLToFile(new URL(url) , new File(fname));
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("WebDownloader 方法出错");
        }
    }
}


















