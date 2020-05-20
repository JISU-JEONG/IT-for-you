import Vue from "vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/Home.vue")
  },
  {
    path: '/login',
    name: 'login',
    component: () => import("../views/Login.vue")
  },
  {
    path: '/admin',
    name: 'Admin',
    redirect: '/admin/user',
    component: () => import("../views/Admin.vue"),
    children: [
      {
        path: 'user',
        name: 'User',
        component: () => import("../views/User.vue"),
      },
      {
        path: 'make',
        name: 'MakeQuestion',
        component: () => import("../views/MakeQuestion.vue"),
      },
      {
        path: 'edit',
        name: 'EditQuestion',
        component: () => import("../views/EditQuestion.vue"),
      },
    ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
