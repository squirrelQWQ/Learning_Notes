<%--
  Created by IntelliJ IDEA.
  User: squirrel
  Date: 2022/4/5
  Time: 20:53
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<!--
个人主页
-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>个人主页</title>
    <style>

    </style>
    <link rel="stylesheet" type="text/css" href="src/css/personalSpace.css">
</head>
<body>
<div>
    <!--头部导航栏-->
    <div id="upper">
        <div id="navigation_bar">
            <ul>
                <!--            浮动在导航栏左侧-->
                <li class="left"><a href="home.html">首页</a></li>

            </ul>
        </div>
    </div>
    <!--主体内容-->
    <div id="middle">
        <!--    左侧的导航栏-->
        <div id="container-left-nav">
            <ul id="left-list">
                <li><a>个人资料</a></li>
                <li><a>我的收藏</a></li>
                <li><a>账号设置</a></li>
            </ul>
        </div>

        <!--    中间的主体内容-->
        <div id="container-main">
            <!--            个人资料界面-->
            <div id="account-data">
                <ul>
                    <li class="data-detail" value="地址">
                        <input name="address">
                    </li>
                    <li class="data-detail" value="电话号码">
                        <input name="phoneNumber">
                    </li>
                    <li class="data-detail" value="用户名">
                        <input name="username">
                    </li>
                    <li class="data-detail" value="密码">
                        <input name="password" type="password">
                    </li>
                    <li class="data-detail">其它</li>
                </ul>

            </div>

            <!--            我的收藏页面-->
            <div id="my-collection"></div>

            <!--            设置账号页面-->
            <div id="account-setting"></div>

        </div>
    </div>

    <!--底部其它信息-->
    <div id="below"></div>

</div>
</body>
</html>
