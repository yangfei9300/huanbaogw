<template>
	<div>
		<div class="colonn">
			<el-carousel :interval="5000" arrow="always" height="900px">
				<el-carousel-item v-for="item in banners" :key="item">
					<img style="width: 100vw;height: 900px;" :src="item" />
				</el-carousel-item>
			</el-carousel>
			<div class="bigviewtongyi roww">
				<div class="colonn" style="    margin-right: 3.125vw;">
					<div class="zhanhuititle" style="margin-bottom: 1.042vw;">
						第10届国际绿色环保产业博览会
					</div>
					<div class="roww" style="margin-bottom: 1.042vw;">
						<div class="zhanhuitime">时间：2024年8月28-30日</div>
						<div class="allline"></div>
						<div class="zhanhuitime">地点：山东省济南市国际会展中心</div>
					</div>
					<div class="zhjianjie">
						为全面推进美丽中国建设，实现碳达峰碳中和，深入打好蓝天碧水净土保卫战，加快推动绿色低碳高质量发展，努力为实现人与自然和谐共生的现代化贡献山东力量，第10届绿色低碳环保产业国际博览会(简称“第10届绿博会”)”将于2024年8月28日30日在山东国际会展中心举办。
						绿博会自2004年举办以来，共吸引来自中国、韩国、日本、美国、欧洲以及香港、台湾等28个国家和地区的2800余家企业和国际组织参加，达成合作意向3000余项，带动产值超过100亿元，对推进区域生态环保产业健康发展，推动环保科技创新、促进绿
						色低碳生活、助力生态文明建设发挥了重要作用。展会以“绿色引领发展，低碳创造未来”为主题，以供需对接为载体，秉承“对接对话、共享共赢”宗旨，围绕山东生态环境减污降碳、协同增效新目标，环保产业科技创新、转型升级新方向，展示低碳减排、环境监测及资源利用新技术、新设备、新服务。
					</div>
				</div>
				<img autoplay
					src="https://shandongtibohui.zsyflive.com/profile/upload/hbgw/f2bb0ac6e0990273bf575da262b18ab.jpg"
					controls class="rightvideoview"></img>
			</div>
		</div>


		<div class="colonn" style="background-color: #e8e8e8;padding: 1.302vw 18.75vw;">
			<div class="" id="title">
				<h1 style="font-size: 2vw;"> 新闻中心 <span style="font-size: 1.5vw;">News Center</span></h1>
				<div class="circle-box"><span class="first-span"></span><span></span></div>
			</div>
			<div class="roww rowsb">
				<video v-for="(item,index) in newVideo" :src="item" controls class="video11"></video>
			</div>
			<div style="height: 40px;"></div>
			<div class="roww">
				<div class="colonn ">
					<img :src="new1" class="leftimg" />
					<div class="colonn">
						<div style="text-align: left;">展会开幕在即！这份参观指南请收好→</div>
						<div style="height: 10px;"></div>
						<div style="text-align: left;"> 2024年8月28日 </div>
					</div>
				</div>
				<div class="colonn allline">
					<div class="listvew" v-for="(item,index) in newsList" 
					@click="toLink(item.url)">{{item.title}}</div>
				</div>
			</div>
			<div style="height: 20px;"></div>
			<!-- <div class="btn-box roww">
				<button class="btnmore">查看更多&gt;&gt;</button>
				<div class="allline"></div>
				<button class="btnmore">更多资讯&gt;&gt;</button>
			</div> -->

		</div>


		<div class="colonn" style="background-color: #ffffff;padding: 1.302vw 18.75vw;">
			<div class="" id="title">
				<h1 style="font-size: 2vw;"> 展览板块 <span style="font-size: 1.5vw;"> Exhibition Section</span></h1>
				<div class="circle-box"><span class="first-span"></span><span></span></div>
			</div>
			<el-carousel arrow="hover" :interval="5000" height="320px">
				<el-carousel-item v-for="item in banners" :key="item">
					<div class="roww center_center">
						<div class="swiper-box colonn " v-for="(item,index) in zhanlanbankuai"><img class="img123"
								:src="item.icon">
							<div class="line" style="width: 30px;height: 1px;background-color: white;margin:20px 0px;">
							</div>
							<div>{{item.title}}</div>
						</div>
					</div>
				</el-carousel-item>
			</el-carousel>
		</div>


		<div class="bigviewtongyi colonn" style="background-color: #e8e8e8;padding: 1.302vw 18.75vw;">
			<div class="" id="title">
				<h1 style="font-size: 2vw;"> 往届精彩 <span style="font-size: 1.5vw;">Previous exciting events</span></h1>
				<div class="circle-box"><span class="first-span"></span><span></span></div>
			</div>
			<el-carousel :interval="4000" type="card" height="300px">
				<el-carousel-item v-for="item in wqjcimgs" :key="item">
					<img style="width: 100%;height: 300px;" :src="item" />
				</el-carousel-item>
			</el-carousel>
		</div>


		<div class="colonn" style="background-color: #ffffff;padding: 1.302vw 18.75vw;">
			<div class="" id="title">
				<h1 style="font-size: 2vw;"> 品牌展商 <span style="font-size: 1.5vw;"> Brand Exhibitor</span></h1>
				<div class="circle-box"><span class="first-span"></span><span></span></div>
			</div>
			<!-- <img  
			:src="ppzsicons"/> -->
			<el-carousel arrow="hover" height="200px" :interval="5000">
				<el-carousel-item v-for="(item,index) in qylogos">
					<div class="huanhang ">
						<div class="hezuomeitoitemimg" style=" margin:0vw 1vw 1vw 1.3vw;"
							v-for="(item1,index1) in item">
							<img class="hezuomeitoitemimg" :src="urlqy+item1">
						</div>
					</div>
				</el-carousel-item>


			</el-carousel>

		</div>


		<div class="colonn" style="background-color: #e8e8e8;padding: 1.302vw 18.75vw;">
			<div class="" id="title">
				<h1 style="font-size: 2vw;"> 合作媒体 <span style="font-size: 1.5vw;">Cooperative Media</span></h1>
				<div class="circle-box"><span class="first-span"></span><span></span></div>
			</div>

			<el-carousel height="200px" :interval="5000">
				<el-carousel-item v-for="(item,index) in mtiLogos" :key="item">
					<div class="huanhang ">
						<div class="hezuomeitoitemimg" style=" margin:0vw 1vw 1vw 1.3vw;"
							v-for="(item1,index1) in item"
							@click="toGw(item1)"
							>
							<img class="hezuomeitoitemimg" :src="url+item1">
						</div>
					</div>
				</el-carousel-item>
				<!-- <el-carousel-item v-for="item in banners" :key="item">
					<div class="huanhang ">
						<div class="hezuomeitoitemimg" style=" margin: 0 1.042vw 1.563vw;" 
						v-for="(item1,index1) in mtiLogos[1]">
							<img class="hezuomeitoitemimg"
								:src="url+item1">
						</div>
					</div>
				</el-carousel-item> -->

			</el-carousel>
		</div>

		<!-- <div class="bigviewtongyi colonn">

			<div class="" id="title">
				<h1 style="font-size: 2vw;"> 友情链接 <span style="font-size: 1.5vw;"> Friendship Link </span></h1>
				<div class="circle-box"><span class="first-span"></span><span></span></div>
			</div>
			<div class="huanhang ">
				<div class="lianjietxt" style="width: 25%;" v-for="(item,index) in 10">中华人民共和国生态环境部</div>
			</div>
		</div> -->

	</div>
</template>

<script>
	export default {
		name: 'Home',

		components: {},

		data() {
			return {
				mtiLogos: [
					['中国泵阀网.png', '中国泵阀网1.png', '中国空分网logo_170x81.jpg', '云推B2B商务网logo_170x81.jpg',
						'云推微商网logo_170x81.jpg', '五金机械网.png', '产业世界.png', '人工智能网 拷贝.png', '代理加盟网logo_170x81.jpg',
						'仪表网 拷贝.png'
					],
					['全球微商网logo_170x81.jpg', '全球环保研究网.png', '净化商城.png', '化工制造网.png', '化工机械设备网170-81 拷贝.png',
						'国际节能环保网 拷贝.png', '展大人.png', '工控之家网logo_170x81.jpg', '必高环保猎头1.png', '新3gwzzj150-70.png'
					],
					['新zdhsbw150-70.jpg', '智能制造网logo171x80.png', '机械信息网.png', '机械商务网.png', '机械工业网.png', '机械行业网.png',
						'机械资讯网.png', '汽车装修网.png', '泵阀制造网 拷贝.png', '火爆会展网.webp.png'
					],
					
					['环保在线 192-90 拷贝.png', '环保居家网.png', '环保时代网 拷贝.png', '生态环境产业网.png', '盘古机械网.png', '绿色节能网.png',
						'聚众果微商网logo_170x81.jpg', '货源代理网_logo170x81.jpg', '食品伙伴网新版logo192-90.png','中国天然气网logo_170x81.jpg'
						// ,'中国制造网LOGO 拷贝.jpg','世界机械网.png', 
					],
					[
						'中国制造网LOGO 拷贝.jpg','世界机械网.png', '1-北极星环保招聘.png', '1-北极星环保网.png', 
					]
				],
				qylogos: [
					['0.png', '1.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png', '16.png', '17.png'],
					['18.png', '19.png', '2.png', '20.png', '21.png', '22.png', '23.png', '24.png', '25.png',
					'26.png'],
					['27.png', '28.png', '29.png', '3.png', '30.png', '31.png', '32.png', '33.png', '34.png',
					'35.png'],
					['36.png', '4.jpg', '5.png', '6.png', '7.png', '8.png', '9.png']
				],
				'url': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/mt/网站图片/',
				'urlqy': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/qylogo/',
				banners: [
					'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/3411a7d84ab6664be54f49af9a1bbd4.jpg',
				],
				newVideo: [
					'https://meili-media.oss-cn-beijing.aliyuncs.com/huanbao/%E5%AE%A3%E4%BC%A0%E7%89%87.mp4',
					"https://meili-media.oss-cn-beijing.aliyuncs.com/huanbao/%E5%AE%A3%E4%BC%A0%E8%A7%86%E9%A2%91%205.31.mp4",
					"https://meili-media.oss-cn-beijing.aliyuncs.com/huanbao/%E5%AE%A3%E4%BC%A0%E8%A7%86%E9%A2%91.mp4",
					// "https://shandongtibohui.zsyflive.com/profile/upload/hbgw/0fd5c408f1293b3e500fd62a83f42b6b.mp4"
				],
				//新闻左边的图片
				'new1': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/new1.jpg',
				'hezuomeiti': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/hezuomeiti.png',
				//新闻列表
				newsList: [
					{
						'title': '第10届国际绿色环保展，预登记，享好礼，您参观我买单！',
						'url': 'https://mp.weixin.qq.com/s?__biz=MzkzODI2MzEwNg==&mid=2247506129&idx=1&sn=50c460b53c7b1ab7cde733ca666e8580&chksm=c2804ffcf5f7c6ea90a53c4b48fa156b7b15467870f5ddfcce4433d71c66637ba3cd7c64d87e#rd'
					},
					{
						'title': '第10届国际绿色环保产业博览会邀请函！',
						'url': 'https://mp.weixin.qq.com/s?__biz=MzkzODI2MzEwNg==&mid=2247506201&idx=1&sn=070aa1db74c672160451a722c23f145b&chksm=c2804e34f5f7c7222e0d9f2d5e55bd05424f9456ad3fdd2955b3d46ed4cd98fe429d7e686e78#rd'
					},
					{
						'title': '第10届国际绿色环保产业博览会--上届回顾',
						'url': 'https://mp.weixin.qq.com/s?__biz=MzkzODI2MzEwNg==&mid=2247506257&idx=1&sn=2ffc84b5670efb13d09ebe374bfbbc79&chksm=c2804e7cf5f7c76af244045fb46f45a52464ddef3be37d04f9f38070acfd43975c1d9b96b546#rd'
					}
					// ,
					// {
					// 	'title': '一图读懂《水污染防治法》所有亮点！',
					// 	'url': 'https://mp.weixin.qq.com/s/i9vfnHLfd2eciMDe47hMUA'
					// },
					// {  
					// 	'title': '环保科普 | 一图读懂生态安',
					// 	'url': 'https://mp.weixin.qq.com/s/SLS14K1zjTBS2mgp08HPXQ'
					// },
				],
				// 展览板块
				'zhanlanbankuai': [{
						'icon': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/ban1.png',
						'title': '水与污水技术及装备展区'
					},
					{
						'icon': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/ban2.png',
						'title': '大气污染治理技术及装备展区'
					}, {
						'icon': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/ban3.png',
						'title': '环境监测仪器及设备展区'
					}, {
						'icon': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/ban4.png',
						'title': '固废处理与资源化利用技术及装备展区'
					}, {
						'icon': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/ban5.png',
						'title': '环境综合服务展区'
					}, {
						'icon': 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/ban6.png',
						'title': '土壤与地下水技术及装备展区'
					}    
				],
				// 往期精彩
				wqjcimgs: [
					'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/wqjc1.jpg',
					'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/wqjc2.jpg',
					'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/wqjc3.jpg',
				],
				// 品牌展商图片
				ppzsicons: "https://shandongtibohui.zsyflive.com/profile/upload/hbgw/pinpaizhanshang.jpg",
				// 合作媒体
				hzmticons: "https://shandongtibohui.zsyflive.com/profile/upload/hbgw/hezuomeiti.png",
			}
		},
		beforeMount() {},
		beforeDestroy() {},
		mounted() {

		},

		methods: {
			// 跳转管网
			toGw(url){
				if(url=="环保时代网 拷贝.png"){
					window.open("http://www.eptimes.cn");
				}else if(url=="38ff9cdacdf25052bc310169344fcc3.jpg"){
					window.open("https://www.ibicn.com");
				}else if(url=="c1b4a7098ed60717091d38a0514ca4d.jpg"){
					window.open("http://www.haozhanhui.com");
				}else if(url=="产业世界.png"){
					window.open("http://www.inwwin.com.cn/1197/");
				}else if(url=="产业世界.png"){
					window.open("http://www.inwwin.com.cn/1197/");
				}else if(url=="全球环保研究网.png"){
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
	.el-carousel__item h3 {
		color: #475669;
		font-size: 18px;
		opacity: 0.75;
		line-height: 300px;
		margin: 0;
	}

	.el-carousel__item:nth-child(2n) {
		/* background-color: #99a9bf; */
	}

	.el-carousel__item:nth-child(2n+1) {
		/* background-color: #d3dce6; */
	}

	.bigviewtongyi {
		padding: 1.302vw 18.75vw;
		color: #333;
		font-size: .833vw;
		margin-right: 3.125vw;
	}

	.rightvideoview {
		width: calc(100%- 36.458vw);
		height: 15.365vw;
	}

	.zhanhuititle {
		font-size: 1.667vw;
		margin-bottom: 1.563vw;
	}

	.zhjianjie {
		line-height: 1.563vw;
		margin-bottom: 1.042vw;
		font-size: 0.8vw;
		width: 36.458vw;
		text-align: left;

	}

	.zhanhuitime {
		color: #0054e1;
		font-size: .938vw;
		font-weight: 600;
	}

	#title {
		display: flex;
		justify-content: space-between;
		padding: 1.042vw 0 0.3vw 0;
		margin-bottom: 2.083vw;
		color: #333;
		font-size: 1.667vw;
		position: relative;
		align-items: flex-end;
		border-bottom: 3px solid #000000;
	}

	.lianjietxt {
		display: flex;
		width: 25%;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 1.042vw;
		font-weight: 600;
		text-align: center;
	}

	.hezuomeitoitemimg {
		width: 10.0vw;
		height: 4.167vw;
		text-align: center;
		/* background: #fff; */
		cursor: pointer;
		z-index: 9999;
	}

	.swiper-box {
		font-size: .833vw;
		background: #0c872b;
		/* background:linear-gradient(to right,#0c872b,#53f255); */
		border-radius: 1.042vw;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 1.563vw 1.042vw;
		margin: 0.521vw 1.563vw;
		height: 11.458vw;
		cursor: pointer;
		color: #fff;
		width: 270px;
	}

	.img123 {
		width: 3.438vw;
	}

	.video11 {
		height: 7vw;
	}

	.leftimg {
		width: 27.083vw;
		height: 15.365vw;
		margin-bottom: 1.042vw;
		margin-right: 5.208vw;
	}

	.listvew {
		border-bottom: 1px solid #b5b2b2;
		line-height: 2.906vw;
		height: 2.906vw;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
		cursor: pointer;
		text-align: left;
	}

	.btnmore {
		border: unset;
		background: unset;
		color: #348942;
		font-size: 1.25vw;
	}
</style>