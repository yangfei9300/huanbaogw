<template>
	<div class="colonn">
		<img src="https://xintfboys.mianshijing.top/img/banner_3.fa38cdc3.jpg" style="width: 100vw;">
		<div class="breadcrumb roww center_center"><img
				src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAqVJREFUSEvNlMtrE2EUxc/5ZpK0lEYUrYjbbkxDkkkiLnRRRGkLCoorV8W14sqViFRa33YhhQoGdSOCCxeu/CPKdJISrY8K9YFQKWpiH6TpzJUvJGFo0yahGwdmM9z7m8O95x6ihae3tzfU1dUVNwzj7/T09AcAXrM2NisAoCzLOkLyNoCC67pXc7nc22Z9zcAqnU6nPc+7T/IoABfA6/X19Wu5XO7jdvDtwEwmk0kA4ySPATA0SERKJF8BuG7b9uet4FuBGY/HE6Zp3gVwvAb1QVYBvHRd90Y2m51vBG8EZiKR0IuqQc1GjSKyDOC5YRg3p6amvm2s2QhmOp3uq870BICGUB+kKCLPROSe4zg//HA/mLFYrM80zVskBwEEmm2+OvM/ADJra2vj+Xx+odZTB1uWFdGWIjnUKtT3418AJgE8tG17UX9nKpUKiMghAGMkBwAEW1G6sUZEfpOcKJfLmZmZme96+wcDgcAVz/POANilX5KqTXgZwKKI/CT5xLbtCUYikWAoFDoAYB/JsyQvAQi3AxaRec/zLiqlFkRk1XGcd/UZ9/f3m0tLS8N6wwD2VBcjJFe0tUjW8sEQkTBJPbJa/2ypVBrI5/N129XBWnlHR8cwyTs+sL6yNwBekFx2XVeUUrsBXBaRw76RzQIYtG376yZX6AQLh8MarMOmohjACoBHruuOZbPZgv4QjUZ7gsHgYwCnfOD3AAbaAovIZLFYHJ2bmytqsGVZ+5RSGRE5vSOwVgxg1LbtiuJYLNZjmmZmx4r/b3B3d/cFpZR2hT6USvZqxSRHaqOIRqP7Q6HQUxEZIllxlYh8EpGTjuN82eQKbbfOzs7zAEaqrhAAOnczhULhQW15qVRqr84Eba9qTusrnS2Xy+f0KW8Ct3NprdT+A4i2NyYPIiAgAAAAAElFTkSuQmCC"
				alt="" style="margin-right:10px;">
			<div>首页 — 观众服务 — 交通指南 </div>
			<div class="allline"></div>
		</div>
		<div data-v-6159cbc4="" id="com-title">
			<div>交通指南</div>
		</div>


		<div id="traffic-guide"
		style="text-align: left;"
		>
		<!-- <iframe
				src="https://ditu.amap.com/search?id=B022715PNV&amp;city=340111&amp;geoobj=117.236396%7C31.735564%7C117.24732%7C31.740926&amp;query_type=IDQ&amp;query=%E5%90%88%E8%82%A5%E6%BB%A8%E6%B9%96%E5%9B%BD%E9%99%85%E4%BC%9A%E5%B1%95%E4%B8%AD%E5%BF%83&amp;zoom=17.5"
				frameborder="0" 
				width="100%" 
				height="360px">
				</iframe> -->
				
			<div class="traffic-box">
				<div class="traffic-line" style="line-height: 30px;">
					<span style="font-size: 1.2vw;">市内乘车推荐</span><br>
					(1)济南东站地铁R3线(济南东站)一八涧堡站(换乘地铁2二环西路站(步行至山东国际会展中心西入口)<br>
					
					(2)济南火车站地铁R2线(济南站北站)二环西路站B口北行600米。<br>
					(3)济南西站地铁R1线(济南西站府张站(换乘地铁R2线二环西路站(步行至山东国际会展中心西入口)<br>
					(4)墙机场济南遥墙国际机场站上车机场巴5号线(始发一济南东站(换乘地铁R3线一八涧堡站(换 地铁R2线二环西路站(步行至山东国际会展中心西入口)<br>
					
					(5)济南长途汽车总站地铁R2线(济洛路站)(F二环西路站(步行至山东国际会展中心西入口)<br>
					
					(6)济地铁线路<br>
				</div>
				<img style="width: 100%;" v-for="(item,index) in jtimgs" :src="item"/>
				<!-- <div class="traffic-line">
					<h5><img src="data:image/png;base64,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"
							alt=""> 合肥高铁南站到达 </h5>
					<p>出租车：线路长度8公里，时间约为20分钟</p>
					<p> 推荐线路:合肥高铁南站距离合肥滨湖国际会展中心约8公里，可乘坐地铁1号线至 ＂滨湖会展中心”站，从B出口出站即可到达。 </p>
				</div>
				<div class="traffic-line">
					<h5><img src="data:image/png;base64,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"
							alt=""> 合肥火车站到达</h5>
					<p>出租车：线路长度18公里，时间约为30分钟</p>
					<p> 推荐线路:合肥火车站距离合肥滨湖国际会展中心约20公里，可乘 坐地铁1号线至 ＂滨湖会展中心” ，从B出口出站即可到达。 </p>
				</div> -->
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
				jtimgs:[
					'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/地铁图.jpg',
					'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/自驾车路线图.png'
				]
				
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




	#traffic-guide {
		margin: 0 18.75vw;
		margin-bottom: 2.604vw;
		border: 1px solid #b5b2b2;
		padding: 3.125vw 4.167vw
	}

	#traffic-guide .traffic-box {
		/* padding-top: 3.125vw */
	}

	#traffic-guide .traffic-box .traffic-line {
		border-bottom: 1px solid #b5b2b2;
		padding: 1.563vw 0
	}

	#traffic-guide .traffic-box .traffic-line h5 {
		display: flex;
		align-items: center;
		font-size: 1.25vw;
		font-weight: 600;
		margin-bottom: .521vw
	}

	#traffic-guide .traffic-box .traffic-line h5 img {
		margin-right: 2.604vw
	}

	#traffic-guide .traffic-box .traffic-line p {
		padding: .781vw 0
	}

	#traffic-guide .traffic-box .traffic-line :last-child {
		border: unset;
		padding-bottom: 0
	}
</style>