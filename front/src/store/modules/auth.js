import api from "../../utils/api";

// state : data와 유사
const state = {
  token: null,
  userInfo: null
};
// mutations : state를 변화시키기 위한 메서드(함수)
const mutations = {
  // 첫번째 인자는 무조건 state
  // 이후 인자는 payload(즉, 임의의 매개변수)
  setToken(state, token) {
    state.token = token;
  },

  setUserInfo(state, userInfo) {
    state.userInfo = userInfo;
  }
};

const actions = {
  // 첫번째 인자는 context (다양한)
  // 이후 인자는 payload(임의의 매개변수)
  login(context, token) {
    // mutation 호출 -> commit
    context.commit("setToken", token);
  },

  logout(context) {
    context.commit("setToken", null);
  },

  async loginCheck(context, token) {
    const logincheck = await api.loginCheck(token);
    context.commit("setUserInfo", logincheck);
  }
};

import jwtDecode from "jwt-decode";

const getters = {
  options(state) {
    return {
      headers: {
        Authorization: `JWT ${state.token}`
      }
    };
  },

  user(state) {
    return jwtDecode(state.token).user_id;
  },

  getUserInfo(state) {
    return state.userInfo;
  }
};

export default {
  state,
  mutations,
  actions,
  getters
};
