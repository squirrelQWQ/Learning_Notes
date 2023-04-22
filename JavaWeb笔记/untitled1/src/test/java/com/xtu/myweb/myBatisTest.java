package com.xtu.myweb;

import com.xtu.myweb.mapper.BrandMapper;
import com.xtu.myweb.pojo.Brand;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.junit.Test;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

/**
 * Created with IntelliJ IDEA.
 *
 * @Author: 陈文杰
 * @Date: 2022/03/26/10:26
 * @Description:
 */
public class myBatisTest {
    /*
    查询brand表全部内容
    * */
    @Test
    public void testSelectAll() throws IOException {
//        获取sqlSessionFactory对象
        String resource = "mybatis-config.xml";
        InputStream inputStream = Resources.getResourceAsStream(resource);
        SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);

//        获取sqlSession对象
        SqlSession sqlSession = sqlSessionFactory.openSession();

//        获取mapper接口代理对象
        BrandMapper brandMapper = sqlSession.getMapper(BrandMapper.class);

//        执行sql语句
        List<Brand> brands = brandMapper.selectAll();
        System.out.println(brands);

//        释放资源
        sqlSession.close();
    }


/*
* 条件查询，根据ID进行查询
* */
    @Test
    public void testSelectById() throws IOException {
//        获取sqlSessionFactory对象
        String resource = "mybatis-config.xml";
        InputStream inputStream = Resources.getResourceAsStream(resource);
        SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
//        获取sqlSession对象
        SqlSession sqlSession = sqlSessionFactory.openSession();
//        获取mapper接口代理对象
        BrandMapper brandMapper = sqlSession.getMapper(BrandMapper.class);
//        执行sql语句
        Brand brand = brandMapper.selectById(1);
        System.out.println(brand);
//        释放资源
        sqlSession.close();
    }


/*
多条件查询
*/
    @Test
    public void testSelectByCondition() throws IOException {
//        接收参数
        int status = 0;
        String companyName = "业";
        String description = "描述";
//        根据业务逻辑处理参数
        companyName = "%"+companyName +"%";
        description = "%"+description +"%";
//        使用对象封装对象
        Brand brand = new Brand();
        brand.setCompanyName(companyName);
        brand.setDescription(description);
        brand.setStatus(status);

//        获取sqlSessionFactory对象
        String resource = "mybatis-config.xml";
        InputStream inputStream = Resources.getResourceAsStream(resource);
        SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
//        获取sqlSession对象
        SqlSession sqlSession = sqlSessionFactory.openSession();
//        获取mapper接口代理对象
        BrandMapper brandMapper = sqlSession.getMapper(BrandMapper.class);
//        执行sql语句
        List<Brand> brands = brandMapper.selectByCondition(brand);
        System.out.println("==========================================================");
        System.out.println(brands);
        System.out.println("==========================================================");
//        释放资源
        sqlSession.close();
    }


    @Test
    public void testAdd() throws IOException {
//        接收参数
        String brandName = "土豆";
        String companyName = "大土豆公司";
        Integer ordered = 12;
        String description = "大土豆革命的描述";
        int status = 0;

//        使用对象封装对象
        Brand brand = new Brand();
        brand.setBrandName(brandName);
        brand.setCompanyName(companyName);
        brand.setOrdered(ordered);
        brand.setDescription(description);
        brand.setStatus(status);

//        获取sqlSessionFactory对象
        String resource = "mybatis-config.xml";
        InputStream inputStream = Resources.getResourceAsStream(resource);
        SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
//        获取sqlSession对象
//        SqlSession sqlSession = sqlSessionFactory.openSession();
        SqlSession sqlSession = sqlSessionFactory.openSession(true);    //开启事务自动提交
//        获取mapper接口代理对象
        BrandMapper brandMapper = sqlSession.getMapper(BrandMapper.class);
//        执行sql语句
        try {
            brandMapper.add(brand);
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println(brand.getId());
        //sqlSession.commit();  openSession()默认不开启事务提交，需要手动提交事务
//        释放资源
        sqlSession.close();
    }

//动态更新代码测试
    @Test
    public void testUpdate() throws IOException {
//        接收参数
        String brandName = "大白菜";
        String companyName = "大白菜公司";
//        Integer ordered = 12;
//        String description = "大土豆革命的描述";
        int status = 1;

//        使用对象封装对象
        Brand brand = new Brand();
        brand.setBrandName(brandName);
        brand.setCompanyName(companyName);
//        brand.setOrdered(ordered);
//        brand.setDescription(description);
        brand.setStatus(status);
        brand.setId(12);

//        获取sqlSessionFactory对象
        String resource = "mybatis-config.xml";
        InputStream inputStream = Resources.getResourceAsStream(resource);
        SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
//        获取sqlSession对象
//        SqlSession sqlSession = sqlSessionFactory.openSession();
        SqlSession sqlSession = sqlSessionFactory.openSession(true);    //开启事务自动提交
//        获取mapper接口代理对象
        BrandMapper brandMapper = sqlSession.getMapper(BrandMapper.class);
//        执行sql语句
        try {
            System.out.println(brandMapper.update(brand));
        } catch (Exception e) {
            e.printStackTrace();
        }
//        释放资源
        sqlSession.close();
    }


    //动态更新代码测试
    @Test
    public void testDelectByIds() throws IOException {
//        接收参数
        int[] ids = {4,5,6};

//        获取sqlSessionFactory对象
        String resource = "mybatis-config.xml";
        InputStream inputStream = Resources.getResourceAsStream(resource);
        SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
//        获取sqlSession对象
        SqlSession sqlSession = sqlSessionFactory.openSession(true);    //开启事务自动提交
//        获取mapper接口代理对象
        BrandMapper brandMapper = sqlSession.getMapper(BrandMapper.class);
//        执行sql语句
        try {
            System.out.println(brandMapper.deleteByIds(ids));
        } catch (Exception e) {
            e.printStackTrace();
        }
//        释放资源
        sqlSession.close();
    }
}










