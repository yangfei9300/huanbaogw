<template>
	<div class="colonn">
		<img src="https://xintfboys.mianshijing.top/img/banner_3.fa38cdc3.jpg" style="width: 100vw;">
		<div class="breadcrumb roww center_center"><img
				src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAqVJREFUSEvNlMtrE2EUxc/5ZpK0lEYUrYjbbkxDkkkiLnRRRGkLCoorV8W14sqViFRa33YhhQoGdSOCCxeu/CPKdJISrY8K9YFQKWpiH6TpzJUvJGFo0yahGwdmM9z7m8O95x6ihae3tzfU1dUVNwzj7/T09AcAXrM2NisAoCzLOkLyNoCC67pXc7nc22Z9zcAqnU6nPc+7T/IoABfA6/X19Wu5XO7jdvDtwEwmk0kA4ySPATA0SERKJF8BuG7b9uet4FuBGY/HE6Zp3gVwvAb1QVYBvHRd90Y2m51vBG8EZiKR0IuqQc1GjSKyDOC5YRg3p6amvm2s2QhmOp3uq870BICGUB+kKCLPROSe4zg//HA/mLFYrM80zVskBwEEmm2+OvM/ADJra2vj+Xx+odZTB1uWFdGWIjnUKtT3418AJgE8tG17UX9nKpUKiMghAGMkBwAEW1G6sUZEfpOcKJfLmZmZme96+wcDgcAVz/POANilX5KqTXgZwKKI/CT5xLbtCUYikWAoFDoAYB/JsyQvAQi3AxaRec/zLiqlFkRk1XGcd/UZ9/f3m0tLS8N6wwD2VBcjJFe0tUjW8sEQkTBJPbJa/2ypVBrI5/N129XBWnlHR8cwyTs+sL6yNwBekFx2XVeUUrsBXBaRw76RzQIYtG376yZX6AQLh8MarMOmohjACoBHruuOZbPZgv4QjUZ7gsHgYwCnfOD3AAbaAovIZLFYHJ2bmytqsGVZ+5RSGRE5vSOwVgxg1LbtiuJYLNZjmmZmx4r/b3B3d/cFpZR2hT6USvZqxSRHaqOIRqP7Q6HQUxEZIllxlYh8EpGTjuN82eQKbbfOzs7zAEaqrhAAOnczhULhQW15qVRqr84Eba9qTusrnS2Xy+f0KW8Ct3NprdT+A4i2NyYPIiAgAAAAAElFTkSuQmCC"
				alt="" style="margin-right:10px;">
			<div>首页 — 观众服务 — 酒店信息 </div>
			<div class="allline"></div>
		</div>
		<div class="colonn" id="com-title">
			<div class="roww">
				<div>酒店信息</div>
				
				<div class="allline"></div>
			</div>
			<div style="height: 5px;"></div>
			<img
			style="width: 100%;"
			:src="jiudianxinxi"/>
		</div>
		
		<div data-v-2ca25781="" id="hotel"><img data-v-2ca25781="" src="https://xintfboys.mianshijing.top/img/hotel.4697ef4f.png" alt=""></div>
		
	</div>
</template>


<script>
	export default {
		name: 'Home',
	
		components: {
		},
	
	
		data() {
			return {
				jiudianxinxi:'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/酒店信息.png',
			}
		},
		beforeMount() {
		},
		beforeDestroy() {},
		mounted() {
	
		},
	
		methods: {
			topage(index) {
				this.$emit('myEvent',{index:index})
			},
			
		}
	}
</script>


<style>
	.breadcrumb {
		height: 3.646vw;
		border-bottom: 1px solid #b5b2b2;
		font-size: .938vw;
		padding: 0 18.75vw;
		display: flex;
		align-items: center;
	}
	
	#overview {
		margin: 0 18.75vw;
		margin-bottom: 2.604vw;
		border: 1px solid #b5b2b2;
	
		padding: 3.125vw 3.646vw;
		text-align: left;
	}
	
	
	
	
	#hotel[data-v-2ca25781] { margin: 0px 18.75vw 2.604vw; border: 1px solid rgb(181, 178, 178); padding: 2.604vw; }
	#hotel img[data-v-2ca25781] { width: 100%; }

</style>