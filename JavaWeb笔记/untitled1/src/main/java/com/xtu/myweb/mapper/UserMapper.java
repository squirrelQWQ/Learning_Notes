package com.xtu.myweb.mapper;

import com.xtu.myweb.pojo.User;

import java.util.List;

/**
 * Created with IntelliJ IDEA.
 *
 * @Author: 陈文杰
 * @Date: 2022/03/26/10:35
 * @Description:
 */
public interface UserMapper {
    List<User> selectAll();
}
