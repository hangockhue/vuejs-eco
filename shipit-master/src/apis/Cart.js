import Api from "./Api"

const END_POINT="api/order/"

export default {
    post() {
        return Api.get(END_POINT);
    },
}
