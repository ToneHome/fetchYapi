import Vue from 'vue';
import App from './App';
import 'element-ui/lib/theme-chalk/index.css';

// 导入插件
import plugin from '@/plugins';
import router from '@/router';
import store from '@/store';

import {
  Input,
  Cascader,
  Table,
  TableColumn,
  Checkbox,
  CheckboxGroup,
  Select,
  Option,
  RadioGroup,
  Radio,
  Dialog,
  Progress,
  Slider,
  Switch
} from 'element-ui';

Vue.use(Input);
Vue.use(Cascader);
Vue.use(Table);
Vue.use(TableColumn);
Vue.use(Checkbox);
Vue.use(CheckboxGroup);
Vue.use(Select);
Vue.use(Option);
Vue.use(Radio);
Vue.use(RadioGroup);
Vue.use(Dialog);
Vue.use(Progress);
Vue.use(Slider);
Vue.use(Switch);

Vue.config.productionTip = false;

Vue.use(plugin);

new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
});
