<template>
	<div class="colonn">
		<img src="https://xintfboys.mianshijing.top/img/banner_3.fa38cdc3.jpg" style="width: 100vw;">
		<div class="breadcrumb roww center_center"><img
				src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAqVJREFUSEvNlMtrE2EUxc/5ZpK0lEYUrYjbbkxDkkkiLnRRRGkLCoorV8W14sqViFRa33YhhQoGdSOCCxeu/CPKdJISrY8K9YFQKWpiH6TpzJUvJGFo0yahGwdmM9z7m8O95x6ihae3tzfU1dUVNwzj7/T09AcAXrM2NisAoCzLOkLyNoCC67pXc7nc22Z9zcAqnU6nPc+7T/IoABfA6/X19Wu5XO7jdvDtwEwmk0kA4ySPATA0SERKJF8BuG7b9uet4FuBGY/HE6Zp3gVwvAb1QVYBvHRd90Y2m51vBG8EZiKR0IuqQc1GjSKyDOC5YRg3p6amvm2s2QhmOp3uq870BICGUB+kKCLPROSe4zg//HA/mLFYrM80zVskBwEEmm2+OvM/ADJra2vj+Xx+odZTB1uWFdGWIjnUKtT3418AJgE8tG17UX9nKpUKiMghAGMkBwAEW1G6sUZEfpOcKJfLmZmZme96+wcDgcAVz/POANilX5KqTXgZwKKI/CT5xLbtCUYikWAoFDoAYB/JsyQvAQi3AxaRec/zLiqlFkRk1XGcd/UZ9/f3m0tLS8N6wwD2VBcjJFe0tUjW8sEQkTBJPbJa/2ypVBrI5/N129XBWnlHR8cwyTs+sL6yNwBekFx2XVeUUrsBXBaRw76RzQIYtG376yZX6AQLh8MarMOmohjACoBHruuOZbPZgv4QjUZ7gsHgYwCnfOD3AAbaAovIZLFYHJ2bmytqsGVZ+5RSGRE5vSOwVgxg1LbtiuJYLNZjmmZmx4r/b3B3d/cFpZR2hT6USvZqxSRHaqOIRqP7Q6HQUxEZIllxlYh8EpGTjuN82eQKbbfOzs7zAEaqrhAAOnczhULhQW15qVRqr84Eba9qTusrnS2Xy+f0KW8Ct3NprdT+A4i2NyYPIiAgAAAAAElFTkSuQmCC"
				alt="" style="margin-right:10px;">
			<div>首页 — 展商服务 — 专业观众 </div>
			<div class="allline"></div>
		</div>
		<div data-v-6159cbc4="" id="com-title">
			<div>专业观众</div>
		</div>
		<div id="p-audience" style="text-align: left;">
			<div class="mian">
				<div>
					<div class="rowsa">
						<img style="width: 33.33%;" src="https://xintfboys.mianshijing.top/img/audience_1.90756833.png"
							alt="">
						<img style="width: 33.33%;" src="https://xintfboys.mianshijing.top/img/audience_1.90756833.png"
							alt="">
						<img style="width: 33.33%;" src="https://xintfboys.mianshijing.top/img/audience_1.90756833.png"
							alt="">
					</div>
					<div class="img-box-row">
						<img style="width: 33.33%;" src="https://xintfboys.mianshijing.top/img/audience_1.90756833.png"
							alt="">
						<img style="width: 33.33%;" src="https://xintfboys.mianshijing.top/img/audience_1.90756833.png"
							alt="">
						<img style="width: 33.33%;" src="https://xintfboys.mianshijing.top/img/audience_1.90756833.png"
							alt="">
					</div>
				</div>
				<ul class="audience-list">
					<li v-for="(item,index) in zygzList">
						<h4>· {{item.title}}</h4>
						<p>{{item.txt}}</p>
					</li>
				</ul>
			</div>
		</div>
	</div>
</template>


<script>
	export default {
		name: 'Home',
		components: {},
		data() {
			return {
				zygzList: [{
					'title': "相关政府部门",
					'txt': "生志环境(厅)局发改委、工信()局、水利水(厅)局自然资源(厅)局住建(厅)局、农业农村(厅)局、经信(厅)局、住建局、城管局、海洋、林草、县乡镇政府等;"
				}, {
					'title': "社会组织",
					'txt': "各行业相关学会、协会、商会、促进会、联盟等;全国各大高校;环科院(所);医院;第三方环境监测机构;重点实验空等组团参展参观;"
				}, {
					'title': "大宗采购商",
					'txt': "重点污染源企业、水务集团、自来水公司、供排水公司、污水处理厂、工业园区、商业街区、市政工程、矿山修复、垃圾处理等;"
				}, {
					'title': "工业观众",
					'txt': "石油、化工、水泥、冶金铜铁、矿产、地质、造纸、印刷、电镀等需要污染治理的各相关工业企业;"
				}, {
					'title': "农业观众",
					'txt': "农业部门、农业环境监测站、农场、合作社、畜牧养殖、农作物种养、农副产品加工等需要污染治理、检测的相关农业单位;"
				}, {
					'title': "工程观众",
					'txt': "建筑集团、房地产公司、园林集团、道路施工等涉及污染防治的工程公司;"
				}, {
					'title': "相关产业",
					'txt': "制造商、代理商、经销商、投融资机构及新闻媒体;试剂、耗材、标准物质、样品前处理、实验空设备等相关单位"
				}]
			}
		},
		beforeMount() {},
		beforeDestroy() {},
		mounted() {

		},

		methods: {
			filesClick(item) {
				window.location.href = item.url;
			}
		}
	}
</script>

<style scoped>
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






	#p-audience .mian {
		margin: 0 18.75vw;
		margin-bottom: 2.604vw;
		border: 1px solid #b5b2b2;
		padding: 2.604vw
	}

	#p-audience .mian .img-box .img-box-row {
		display: flex
	}

	#p-audience .mian .img-box .img-box-row div {
		margin: .104vw
	}

	/* #p-audience .mian .img-box  img {
		width: 100%;
		height: 100%;
	} */

	#p-audience .mian .audience-list {
		margin-top: 1.042vw
	}

	#p-audience .mian .audience-list li {
		padding: 1.042vw 0;
		border-bottom: 1px solid #b5b2b2
	}

	#p-audience .mian .audience-list li h4 {
		display: flex;
		align-items: center;
		font-size: .938vw;
		font-weight: 600;
		margin-bottom: .521vw
	}

	#p-audience .mian .audience-list li h4 :before {
		content: "";
		width: .521vw;
		height: .521vw;
		border-radius: .521vw;
		background: #0054e0;
		display: block;
		margin-right: .521vw
	}

	#p-audience .mian .audience-list li :last-child {
		border-bottom: unset
	}
</style>