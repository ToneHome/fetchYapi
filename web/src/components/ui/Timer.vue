<template>
  <div class="timer-panel">
    <i class="icon iconfont iconfont-time">
      <span>{{durations.displayValue}}</span>
    </i>
  </div>
</template>

<script>
import { formatTime } from '@/utils/index.js';

export default {
  name: 'Timer',
  props: {
    costTime: {
      type: Number,
      default: 0
    }
  },
  // data() {
  //   return {
  //     duration: this.costTime
  //   }
  // },
  mounted() {
    this.start();
  },
  methods: {
    start: function() {
      this.durations.seconds++;
      setTimeout(() => {
        this.start();
      }, 1000);

      this.$emit('update:costTime', this.durations.seconds);
    }
  },
  computed: {
    durations: function() {
      return {
        seconds: this.costTime,
        displayValue: formatTime(this.costTime)
      };
    }
  }
  // watch: {
  //   costTime: function() {
  //     debugger
  //   }
  // }
};
</script>

<style lang="less" rel="stylesheet/less">
.timer-panel {
  color: #00b4ff;
  display: inline-block;
  vertical-align: middle;
  .iconfont-time {
    font-size: 26px;
    span {
      font-size: 22px;
      margin-left: 6px;
      height: 30px;
      line-height: 30px;
      vertical-align: middle;
    }
  }
}
</style>
