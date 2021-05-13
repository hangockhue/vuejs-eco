import Api from "./Api";

const END_POINT = 'api/hightlight/';

export default {
    all() {
        return Api.get(END_POINT);
    },
}
