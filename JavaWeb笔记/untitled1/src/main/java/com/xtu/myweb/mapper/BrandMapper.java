package com.xtu.myweb.mapper;

import com.xtu.myweb.pojo.Brand;
import org.apache.ibatis.annotations.Param;

import java.util.List;

/**
 * Created with IntelliJ IDEA.
 *
 * @Author: 陈文杰
 * @Date: 2022/03/26/13:30
 * @Description:
 */
public interface BrandMapper {
//    查询所有
    List<Brand> selectAll();

    Brand selectById(int id);

//    List<Brand> selectByCondition(@Param("status")int status , @Param("companyName") String companyName , @Param("description") String description);

    List<Brand> selectByCondition(Brand brand);
//添加
    void add(Brand brand);

    int update(Brand brand);

    int deleteByIds(@Param("ids") int[] ids);
}








