<template>
	<div class="colonn">
		<img src="https://xintfboys.mianshijing.top/img/banner_3.fa38cdc3.jpg" style="width: 100vw;">
		<div class="breadcrumb roww center_center"><img
				src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAqVJREFUSEvNlMtrE2EUxc/5ZpK0lEYUrYjbbkxDkkkiLnRRRGkLCoorV8W14sqViFRa33YhhQoGdSOCCxeu/CPKdJISrY8K9YFQKWpiH6TpzJUvJGFo0yahGwdmM9z7m8O95x6ihae3tzfU1dUVNwzj7/T09AcAXrM2NisAoCzLOkLyNoCC67pXc7nc22Z9zcAqnU6nPc+7T/IoABfA6/X19Wu5XO7jdvDtwEwmk0kA4ySPATA0SERKJF8BuG7b9uet4FuBGY/HE6Zp3gVwvAb1QVYBvHRd90Y2m51vBG8EZiKR0IuqQc1GjSKyDOC5YRg3p6amvm2s2QhmOp3uq870BICGUB+kKCLPROSe4zg//HA/mLFYrM80zVskBwEEmm2+OvM/ADJra2vj+Xx+odZTB1uWFdGWIjnUKtT3418AJgE8tG17UX9nKpUKiMghAGMkBwAEW1G6sUZEfpOcKJfLmZmZme96+wcDgcAVz/POANilX5KqTXgZwKKI/CT5xLbtCUYikWAoFDoAYB/JsyQvAQi3AxaRec/zLiqlFkRk1XGcd/UZ9/f3m0tLS8N6wwD2VBcjJFe0tUjW8sEQkTBJPbJa/2ypVBrI5/N129XBWnlHR8cwyTs+sL6yNwBekFx2XVeUUrsBXBaRw76RzQIYtG376yZX6AQLh8MarMOmohjACoBHruuOZbPZgv4QjUZ7gsHgYwCnfOD3AAbaAovIZLFYHJ2bmytqsGVZ+5RSGRE5vSOwVgxg1LbtiuJYLNZjmmZmx4r/b3B3d/cFpZR2hT6USvZqxSRHaqOIRqP7Q6HQUxEZIllxlYh8EpGTjuN82eQKbbfOzs7zAEaqrhAAOnczhULhQW15qVRqr84Eba9qTusrnS2Xy+f0KW8Ct3NprdT+A4i2NyYPIiAgAAAAAElFTkSuQmCC"
				alt="" style="margin-right:10px;">
			<div>首页 — 关于展会 — 展览板块 </div>
			<div class="allline"></div>
		</div>
		
		
		<div data-v-6159cbc4="" id="com-title">
			<div>展览板块</div>
		</div>
		
		<div id="overview" class="colonn">
			
			<div class="colonn" v-for="(item,index) in zhanlanbankuai" style="margin-bottom: 1.563vw;">
				<div class="roww titleview center_center">
					<img  class="leftimgg" :src="item.icon"  />
					<div style="color: #348e42;font-size: 25px;">{{item.title}}</div>
					<div class="allline"></div>
				</div>
				<div style="text-align: left;">
					{{item.txt}}
				</div>
			</div>
			
		</div>
		
	</div>
</template>


<script>
	export default {
		name: 'Home',

		components: {
		},


		data() {
			return {
				'zhanlanbankuai': [{
						'icon': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/ban1.png',
						'title': '环境综合服务展区',
						'txt':'环境影响评价、环保管家服务、清洁生产、智慧环保、环境医院等环境综合咨询服务及国际环境综合展示;新能源和可再生能源、新材料、节能产品、技术及服务等。'
					},
					{
						'icon': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/ban2.png',
						'title': '水与污水处理技术及装备展区',
						'txt':'城镇污水处理及资源化利用、工业废水处理、水生态环境修复、农村和畜禽污水处理、海水淡化处理、污泥处理处置、水处理设备、膜与膜组件、过滤压滤、药剂、材料、泵阀管等o'
					}, {
						'icon': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/ban3.png',
						'title': '大气污染治理技术及装备展区',
						'txt':'工业烟尘/粉尘/废气回收与治理、VOCS综合治理、脱硫脱硝、移动源污染治理、恶臭污染治理、无组织排放控制、室内空气净化、大气污染治理设备等。'
					}, {
						'icon': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/ban4.png',
						'title': '环境监测检及应急装备与技术展区',
						'txt':'水、大气、土壤等环境监测与检测、在线检测与控制、环境污染应急监测、实验室设备仪器、噪声与振动控制、室内环境检测与监测服务等。'
					}, {
						'icon': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/ban5.png',
						'title': '固废处理及资源化利用',
						'txt':'一般工业固废综合利用、危险废物处理处置、垃圾分类收集及回收、医疗垃圾、生活垃圾、餐厨垃圾、农废处理等资源化回收利用。'
					}, {
						'icon': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/ban6.png',
						'title': '土壤、地下水及环境修复',
						'txt':'农用地安全利用与修复、工业污染地块风险管控与修复、矿山生态修复、调查与风险评土壤和地下水修复设备等。'
					}
				],
			}
		},
		beforeMount() {},
		beforeDestroy() {},
		mounted() {

		},

		methods: {
			
		}
	}
</script>


<style>
	@import url(../css/ab_zhbk.css);
</style>