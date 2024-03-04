import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)


import Vue from 'vue'
import { BootstrapVue } from 'bootstrap-vue'

import './app.scss'

Vue.use(BootstrapVue)


function showSecondForm() {
    var firstForm = document.getElementById("sign-up");
    var secondForm = document.getElementById("second-form");
    firstForm.style.display = "none";
    secondForm.style.display = "block";
}