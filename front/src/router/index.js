import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store/index";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    redirect: "/IT_For_You",
    component: () => import("../views/Main/SideBar.vue"),
    children: [
      {
        path: "/IT_For_You",
        name: "IT_For_You",
        component: () => import("../views/Main/IT_For_You.vue")
      },
      {
        path: "/category",
        name: "Category",
        component: () => import("../views/Question/Category.vue")
      },
      {
        path: "/interview",
        name: "Interview",
        redirect: "/interview/category",
        component: () => import("../views/InterviewMain.vue"),
        children: [
          {
            path: "category",
            name: "InterviewCategory",
            component: () => import("../views/InterviewCategory.vue")
          },
          {
            path: "list",
            name: "InterviewList",
            component: () => import("../views/InterviewList.vue")
          },
          {
            path: "mynote",
            name: "InterviewMyNote",
            component: () => import("../views/InterviewMyNote.vue")
          }
        ]
      },
      {
        path: "/problem",
        name: "problem",
        component: () => import("../components/Question/Problem.vue")
      },
      {
        path: "/wrongNote",
        name: "wrongNote",
        component: () => import("../views/Note/WrongNote.vue")
      },
      {
        path: "/IT_Note",
        name: "IT_Note",
        component: () => import("../views/Note/IT_Note.vue")
      }
    ]
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/Login/Login.vue")
  },
  {
    path: "/admin",
    name: "Admin",
    redirect: "/admin/user",
    component: () => import("../views/Admin.vue"),
    children: [
      {
        path: "user",
        name: "User",
        component: () => import("../views/User.vue")
      },
      {
        path: "make",
        name: "MakeQuestion",
        component: () => import("../views/MakeQuestion.vue")
      },
      {
        path: "edit",
        name: "EditQuestion",
        component: () => import("../views/EditQuestion.vue")
      }
    ]
  },
  {
    path: "*",
    redirect: "/"
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 };
  }
});

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem("vue-session-key") === null) {
    if (to.path === "/login") {
      return next();
    } else {
      return next("/login");
    }
  }
  const token = JSON.parse(sessionStorage.getItem("vue-session-key"))["jwt"];
  let isLogin = false;
  // 세션이 없을경우 로그인페이지로
  if (token === undefined) {
    // 이동할 페이지가 login일경우 이동가능하게(무한루프 방지)
    if (to.path === "/login") {
      return next();
    }

    // 이동할 페이지가 login이 아닐경우 login페이지로 변경
    else {
      return next("/login");
    }
  }
  store.dispatch("loginCheck", token);
  setTimeout(() => {
    isLogin = store.getters.getUserInfo;
    // 토큰만료시
    if (isLogin === null) {
      if (to.path === "login") {
        return next();
      }

      // 이동할 페이지가 login이 아닐경우 login페이지로 변경
      return next("/login");
    } else {
      if (to.path === "/admin/user" && !isLogin.is_superuser) {
        return next("/");
      }
      if (to.path === "login") {
        return next("/");
      }

      if (to.path === "/problem") {
        const vuexCheck = store.getters.questionList;
        // console.log(vuexCheck);
        if (vuexCheck !== null) {
          next();
        } else {
          next("/");
          console.log(vuexCheck);
        }
      } else if (to.path === "/interview/list") {
        const vuexCheck = store.getters.interviewList;
        // console.log(vuexCheck);
        if (vuexCheck !== null) {
          next();
        } else {
          next("/");
          console.log(vuexCheck);
        }
      } else {
        return next();
      }
    }
  }, 1000);
});

export default router;
