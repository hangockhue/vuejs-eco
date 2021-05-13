
import Api from "./Api";

const END_POINT = 'api/categorys/';

export default {
    all() {
        return Api.get(END_POINT);
    },
}
