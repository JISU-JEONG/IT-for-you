import axios from "@/api/api.service.js";

const getLoginCheck = token => {
  const options = {
    headers: {
      Authorization: `JWT ${token}` // JWT 다음에 공백있음.
    }
  };

  return axios
    .post("/api/accounts/user/", {}, options)
    .then(({ data }) => {
      return data;
    })
    .catch(error => {
      return error.response;
    });
};

export default {
  async loginCheck(token) {
    return await getLoginCheck(token);
  }
};
