<template>
  <div class="form">
    <input type="text" v-model="apiBaseUrl" />
    <input type="text" v-model="apiProjectId" id="" />
    <input type="text" v-model="username" id="" />
    <input type="password" v-model="password" id="" />
    <button @click="search">查询</button>
  </div>
</template>
<script>
export default {
  data() {
    return {
      apiBaseUrl: 'http://yapi.demo.qunar.com',
      apiProjectId: 37254,
      username: '',
      password: ''
    };
  },
  methods: {
    search() {
      let params = {
        apiBaseUrl: this.apiBaseUrl,
        apiProjectId: this.apiProjectId,
        username: this.username,
        password: this.password
      };
      this.$api['fetch/search'](params).then(rs => {
        console.log(rs);
      });
    }
  }
};
</script>
<style lang="less" scoped>
.form {
  width: 780px;
  margin: 0 auto;
}

input {
  width: 100%;
  height: 30px;
  border: 1px solid #dcdcdc;
  margin-top: 15px;
  padding-left: 15px;
}
button {
  margin-top: 15px;
  border: none;
  background: #452891;
  color: #fff;
  width: 140px;
  height: 30px;
  transition: all 0.3s;
  &:active {
    background: #321d69;
  }
  &:focus {
    outline: none;
  }
}
</style>
