import Vue from "vue"
import App from "./App/_App.vue"

new Vue({
    render: handler => handler(App)
}).$mount("#app")