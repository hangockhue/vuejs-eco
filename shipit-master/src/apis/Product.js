import Api from "./Api";

export default {
    all() {
        return Api.get('api/products/');

    },
    show(id) {
        return Api.get(`api/products/${id}/`);
    }
}
