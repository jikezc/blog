import Vue from "vue"
import Router from "vue-router"
import Home from "@/components/Home"
import Support from "../components/Support";
import Article from "../components/Article";
import ArticleDetail from "../components/ArticleDetail";
import MessageBoard from "../components/MessageBoard";
import About from "../components/About";
import mavonEditor from 'mavon-editor';
import 'mavon-editor/dist/css/index.css';

// 这里导入可以让让用户访问的组件


Vue.use(Router);
Vue.use(mavonEditor);

export default new Router({
  // 设置路由模式为'history'，去掉默认的#
  mode: "history",
  routes:[
    //路由列表
    {
      name: "Home",
      path: "/",
      component: Home,
    },
    {
      name: "Home",
      path: "/home",
      component: Home,
    },
    {
      name: "Support",
      path: "/support",
      component: Support,
    },
    {
      name: "Article",
      path: "/article",
      component: Article,
    },
    {
      name: "ArticleDetail",
      path: "/articledetail",
      component: ArticleDetail
    },
    {
      name: "MessageBoard",
      path: "/messageboard",
      component: MessageBoard
    },
    {
      name: "About",
      path: "/about",
      component: About,
    }
  ]
})
