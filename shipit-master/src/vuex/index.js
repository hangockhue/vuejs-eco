import Vue from 'vue';
import Vuex from "vuex";

Vue.use(Vuex);

import cart from "./modules/cart";
import categorys from './modules/categorys';
import product from './modules/product';
import authencation from './modules/authencation'


export default new Vuex.Store({
        modules: {
                product,
                categorys,
                cart,
                authencation,
        }
});