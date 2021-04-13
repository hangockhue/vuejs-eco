import state from "./state";

const LOGIN_SUCCESS = (state, response) => {
    localStorage.setItem('token', response.access)
    state.token = response.access;
    state.user = response.username;
    state.isAuthenticated = true;
    state.isLoading =  false;
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
    state.isAuthenticated = false;
    state.isAuthenticated = false;
    state.isLoading = false;
}

const USER_LOADED = () => {

}

const ERROR = (state, error) => {
    console.log(error)
}
export default {
    LOGIN_SUCCESS,
    ERROR,
    LOGOUT_SUCCESS,
}