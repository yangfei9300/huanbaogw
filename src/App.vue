<template>
	<div id="app">
		<!-- <div @click="toHome">首页</div>
		<router-view></router-view> -->
		<router-view></router-view>
	</div>
</template>

<script>
	export default {
		name: 'app',
		components: {},  
		created() {
			// this.toHome();
			if (this._isMobile()) {
				window.location.href="https://lshbz.com/h5/";
			} 
		},
		methods: {
			toHome() {
				this.$router.push("/about");
			},
			_isMobile() {
				let flag = navigator.userAgent.match(
					/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i
					)
				return flag;
			}
		}
	}
</script>

<style>
	@import url(static/style/style.css);

	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
		/* margin-top: 60px; */
	}

	body {
		padding: 0px;
		margin: 0px;
	}
</style>