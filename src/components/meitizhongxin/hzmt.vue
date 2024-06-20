<template>
	<div class="colonn">
		<img src="https://xintfboys.mianshijing.top/img/banner_3.fa38cdc3.jpg" style="width: 100vw;">
		<div class="breadcrumb roww center_center"><img
				src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAqVJREFUSEvNlMtrE2EUxc/5ZpK0lEYUrYjbbkxDkkkiLnRRRGkLCoorV8W14sqViFRa33YhhQoGdSOCCxeu/CPKdJISrY8K9YFQKWpiH6TpzJUvJGFo0yahGwdmM9z7m8O95x6ihae3tzfU1dUVNwzj7/T09AcAXrM2NisAoCzLOkLyNoCC67pXc7nc22Z9zcAqnU6nPc+7T/IoABfA6/X19Wu5XO7jdvDtwEwmk0kA4ySPATA0SERKJF8BuG7b9uet4FuBGY/HE6Zp3gVwvAb1QVYBvHRd90Y2m51vBG8EZiKR0IuqQc1GjSKyDOC5YRg3p6amvm2s2QhmOp3uq870BICGUB+kKCLPROSe4zg//HA/mLFYrM80zVskBwEEmm2+OvM/ADJra2vj+Xx+odZTB1uWFdGWIjnUKtT3418AJgE8tG17UX9nKpUKiMghAGMkBwAEW1G6sUZEfpOcKJfLmZmZme96+wcDgcAVz/POANilX5KqTXgZwKKI/CT5xLbtCUYikWAoFDoAYB/JsyQvAQi3AxaRec/zLiqlFkRk1XGcd/UZ9/f3m0tLS8N6wwD2VBcjJFe0tUjW8sEQkTBJPbJa/2ypVBrI5/N129XBWnlHR8cwyTs+sL6yNwBekFx2XVeUUrsBXBaRw76RzQIYtG376yZX6AQLh8MarMOmohjACoBHruuOZbPZgv4QjUZ7gsHgYwCnfOD3AAbaAovIZLFYHJ2bmytqsGVZ+5RSGRE5vSOwVgxg1LbtiuJYLNZjmmZmx4r/b3B3d/cFpZR2hT6USvZqxSRHaqOIRqP7Q6HQUxEZIllxlYh8EpGTjuN82eQKbbfOzs7zAEaqrhAAOnczhULhQW15qVRqr84Eba9qTusrnS2Xy+f0KW8Ct3NprdT+A4i2NyYPIiAgAAAAAElFTkSuQmCC"
				alt="" style="margin-right:10px;">
			<div>首页 — 媒体中心 — 合作媒体 </div>
			<div class="allline"></div>
		</div>
		<div data-v-6159cbc4="" id="com-title">
			<div>合作媒体</div>
		</div>


		<div id="media-associated">
			<!-- <img :src="hzmticons" style="width: 100%;" /> -->
			<ul>
				<li v-for="(item,index) in mtiLogos">
					<img :src="url+item" alt=""
					@click="toGw(item)"
					></li>
				
			</ul>
			<p class="tip">*以上排名不分先后顺序</p>
		</div>


	</div>

</template>

<script>
	'hezuomeiti': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/hezuomeiti.png',
</script>


<script>
	export default {
		name: 'Home',

		components: {},


		data() {
			return {
				'url':'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/mt/网站图片/',
				
				// 合作媒体
				hzmticons: "https://shandongtibohui.zsyflive.com/profile/upload/hbgw/hezuomeiti.png",
				mtiLogos: [
					'38ff9cdacdf25052bc310169344fcc3.jpg',
					"e1964aea281c53e716ca5f28d438996.jpg",
					'c1b4a7098ed60717091d38a0514ca4d.jpg',
					'不锈机械网.jpg',
					'fa80b4a6962998c85aa811fa0aa188e.jpg',
					'1-北极星环保网.jpg',
					'1-北极星环保招聘.jpg',
					'91zdh150-70.jpg',
					'BOSS俱乐部.jpg',
					'BtoB网站大全.png',
					'FSC.jpg',
					'zhzx150-70.png',
					'泵阀制造网.png',
					'必高环保猎头1.jpg',
					'博宇保温网.gif',
					'博宇壁纸网.gif',
					'博宇地坪网.gif',
					'博宇防水网.gif',
					'博宇建材网.jpg',
					'博宇涂料网.gif',
					'产业世界.jpg',
					'代理加盟网logo_170x81.jpg',
					'工控之家网logo_170x81.jpg',
					'国际节能环保网.png',
					'化工机械设备网170-81.png',
					'化工制造网.jpg',
					'环保家居网.jpg',
					'环保居家网.png',
					'环保时代网.png',
					'环保在线 192-90.png',
					'会展港.gif',
					'火爆会展网.webp.jpg',
					'货源代理网_logo170x81.jpg',
					'机械工业网.png',
					'机械商务网.png',
					'机械信息网.png',
					'机械行业网.png',
					'机械资讯网.png',
					'净化商城.jpg',
					'聚众果微商网logo_170x81.jpg',
					'绿色节能网.png',
					'能源界.png',
					'盘古机械网.jpg',
					'汽车装修网.png',
					'全球环保研究网.jpg',
					'全球微商网logo_170x81.jpg',
					'人工智能网.png',
					'生态环境产业网.jpg',
					'食品伙伴网新版logo192-90.jpg',
					'世界机械网.png',
					'五金机械网.png',
					'新3gwzzj150-70.png',
					'新zdhsbw150-70.jpg',
					'仪表网.png',
					'云推B2B商务网logo_170x81.jpg',
					'云推微商网logo_170x81.jpg',
					'展大人.jpg',
					'智能制造网logo171x80.jpg',
					'中国泵阀网.gif',
					'中国泵阀网1.jpg',
					'中国空分网logo_170x81.jpg',
					'中国天然气网logo_170x81.jpg',
					'中国制造网LOGO.jpg',
					'装配式建筑网.gif',
				],
			}
		},
		beforeMount() {},
		beforeDestroy() {},
		mounted() {

		},

		methods: {
			// 跳转管网
			toGw(url){
				
				if(url=="环保时代网.png"){
					window.open("http://www.eptimes.cn");
				}else if(url=="38ff9cdacdf25052bc310169344fcc3.jpg"){
					window.open("https://www.ibicn.com");
				}else if(url=="c1b4a7098ed60717091d38a0514ca4d.jpg"){
					window.open("http://www.haozhanhui.com");
				}else if(url=="产业世界.jpg"){
					window.open("http://www.inwwin.com.cn/1197/");
				}else if(url=="全球环保研究网.jpg"){
					window.open("http://www.gepresearch.com/");
				}else if(url=="新3gwzzj150-70.png"){
					window.open("http://www.3gwzzj.zdhsbw.com/");
				}else if(url=="zhzx150-70.png"){
					window.open("http://www.zhzx.zdhsbw.com/");
				}else if(url=="新zdhsbw150-70.jpg"){
					window.open("http://www.zdhsbw.com/");
				}else if(url=="91zdh150-70.jpg"){
					window.open("http://www.91zdh.com");
				}else if(url=="不锈机械网.jpg"){
					window.open("http://www.isbxg.com/");
				}else if(url=="fa80b4a6962998c85aa811fa0aa188e.jpg"){
					window.open("https://www.sdeeppa.com/");
				}
			},
			toLink(url) {
				window.open(url);
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

	li {
		list-style-type: none;
	}





	#media-associated {
		margin: 0 18.75vw;
		margin-bottom: 2.604vw;
		border: 1px solid #b5b2b2;
		padding: 2.604vw 2.083vw
	}

	#media-associated ul {
		display: flex;
		flex-wrap: wrap
	}

	#media-associated ul li {
		width: 20%;
		padding: 0 .781vw;
		box-sizing: border-box;
		margin-bottom: .781vw
	}

	#media-associated ul li img {
		width: 100%;
		height: 4.167vw
	}

	#media-associated .tip {
		text-align: right;
		padding: 0 .781vw
	}
</style>