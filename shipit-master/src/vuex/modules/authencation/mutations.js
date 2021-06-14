import state from "./state";

const LOGIN_SUCCESS = (state, response) => {
    // localStorage.setItem('token', response.access)
    state.token = response.access;
    state.user = response.username;
    state.id = response.id
    state.isAuthenticated = true;
    state.isLoading =  false;
}

const REFRESHTOKEN = (state, response) => {
  state.token = response.access
}

const USER_LOADING = () => {
     state.isLoading = true;
     state.isAuthenticated = false;
}

const LOGIN_FAIL = () => {
    state.token = null;
    state.user = null;
    state.isAuthenticated = false;
    state.isLoading = false;
}

const LOGOUT_SUCCESS = () => {
    state.token = null;
    state.user = null;
    state.isAuthenticated = null;
    state.isLoading = false;
    window.localStorage.removeItem("token");

}

const USER_LOADED = () => {

}


const SET_USERINFOR = (state, response) => {
    state.userInfor = response
}

const ERROR = (state, error) => {
    console.log(error)
}
export default {
    LOGIN_SUCCESS,
    ERROR,
    LOGOUT_SUCCESS,
    SET_USERINFOR,
}
