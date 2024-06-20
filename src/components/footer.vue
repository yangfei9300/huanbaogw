<template>
	<div>
		<div class="colonn">


			<div class="viewbig roww">
				<div class="roww">
					<div class="colonn">
						<div class="baotio">关于展会</div>
						<div class="titilemore"  @click.stop="topage(0)">展会概况</div>
						<div class="titilemore" @click.stop="topage(1)">展览板块</div>
						<div class="titilemore" @click.stop="topage(2)">展区分布</div>
						<div class="titilemore" @click.stop="topage(3)">组织单位</div>
						<div class="titilemore" @click.stop="topage(4)">下载中心</div>
					</div>
					
					<div style="width: 0.5vw;"></div>
					<div class="colonn">
						<div class="baotio">观众服务</div>
						<div class="titilemore"   @click.stop="topage(11)">参观手册</div>
						<div class="titilemore"   @click.stop="topage(12)">交通指南</div>
						<div class="titilemore"   @click.stop="topage(13)">酒店信息</div>
					</div>
					<div style="width: 0.5vw;"></div>
					<div class="colonn">
						<div class="baotio">同期活动</div>
						<div class="titilemore"  @click.stop="topage(16)">高峰论坛</div>
					</div>
					<!-- <div style="width: 0.5vw;"></div>
				<div class="colonn">
					<div class="baotio">同期展会</div>
					<div class="titilemore">水博会</div>
					<div class="titilemore">光储展</div>
				</div> -->
					<div style="width: 0.5vw;"></div>
					<div class="colonn">
						<div class="baotio">媒体中心</div>
						<div class="titilemore"  @click.stop="topage(24)">合作媒体</div>
					</div>
					<div style="width: 0.5vw;"></div>
					<div class="colonn">
						<div class="baotio">联系我们</div>
						<div class="titilemore ">参展热线： 15098772468</div>
						<div class="titilemore">联系人：媒体合作 19563472521</div>
						<div class="titilemore">地址：山东国际会展中心（济南市槐荫区日照路1号）</div>
					</div>
				</div>
				<div class="col-box flex roww">
					<div class="img-box1"><img class="img-box" :src="douyin" style="border-radius: 50%;" alt="">
						<div>抖音号</div>
					</div>
					<div class="img-box1"><img class="img-box" :src="gongzhonghao" alt="">
						<div>公众号</div>
					</div>
					<div class="img-box1"><img class="img-box" :src="xiaochengxu" alt="">
						<div>小程序</div>
					</div>   
				</div>
			</div>
			<div  style="background: #4d4d4d;color: white;height: 20px;"></div>
			<div class="roww center_center" style="background: #4d4d4d;color: white;">
				<img  src="https://beian.mps.gov.cn/img/logo01.dd7ff50e.png" 
				style="width: 20px;height: 20px;"/>
				<div style="width: 10px;"></div>
				<div>鲁ICP备20032105号-3</div>
			</div>
			<div  style="background: #4d4d4d;color: white;height: 20px;"></div>
		</div>
	</div>
</template>

<script>
	import topview from '../components/topview.vue';
	import footerview from '../components/footer.vue';
	import topmenus from '../components/topmenus.vue';
	export default {
		name: 'Home',

		components: {
			topview,
			footerview,
			topmenus
		},


		data() {
			return {

				douyin: 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/douiyinqr.png',
				gongzhonghao: 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/gongzhohnghao.png',
				xiaochengxu: 'https://shandongtibohui.zsyflive.com/profile/upload/hbgw/xiaocehnxgu.png',
			}
		},
		beforeMount() {},
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
	.viewbig {
		color: #fff;
		padding: 1.042vw 10.75vw;
		background: #4d4d4d;
		font-size: 1.042vw;
	}

	.img-box {
		width: 8.333vw;
		height: 8.333vw;
		margin-left: 0.521vw;
		margin-bottom: 0.521vw;
	}

	.img-box1 {
		height: 10.333vw;
	}

	.baotio {
		margin-bottom: 0.781vw;
		font-size: 0.842vw;
		font-weight: 600;
		text-align: left;

	}

	.titilemore {
		margin-bottom: 0.521vw;
		cursor: pointer;
		text-align: left;
		font-size: 0.842vw;
	}
</style>