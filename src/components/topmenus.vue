<template>
	<div>
		<div class="roww center_center" style="padding: 1.042vw 16.063vw;">
			
			<div class="colonn">
				<div class="roww center_center">
					<img class="timeivon"
						src="data:image/png;base64,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" />
					<div>2024年8月28-30日</div>
					<div class="allline"></div>
				</div>
				<div style="height: 10px;"></div>
				<div class="roww center_center">
					<img class="timeivon" data-v-4b7f4818=""
						src="data:image/png;base64,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"
						alt="">
					<div style="flex-shrink: 0;">山东国际会展中心</div>
					<div class="allline"></div>
				</div>
			</div>
			<div style="width: 2vw;"></div>
			<div class="roww">
				<div class="colonn menuswidth">
					<div  @click.stop="topage(26)">首页</div>
				</div>
				<div class="colonn menuswidth">
					<div>关于展会</div>
					<div class="colonn gyzhview" style="position: absolute;top:0px;width: 7vw;z-index: 99999;">
						<div class="noselmenbrsus">关于展会</div>
						<div class="noselmen"  @click.stop="topage(0)">展会概况</div>
						<div class="noselmen" @click.stop="topage(1)">展览模块</div>
						<div class="noselmen" @click.stop="topage(2)">展区分布</div>
						<div class="noselmen" @click.stop="topage(3)">组织单位</div>
						<div class="noselmenbrsuslast" @click.stop="topage(4)">下载中心</div>
					</div>
				</div>
				<!-- <div class="colonn menuswidth">
					<div>展商服务</div>
					<div class="colonn gyzhview" style="position: absolute;top:0px;width: 7vw;z-index: 99999;">
						<div class="noselmenbrsus" >展商服务</div>
						<div class="noselmen"  @click.stop="topage(6)">为何参展</div>
						<div class="noselmen" @click.stop="topage(7)">赞助推广</div>
						<div class="noselmen" @click.stop="topage(8)">展商手册</div>
						<div class="noselmen" @click.stop="topage(9)">专业观众</div>
					</div>
				</div> -->
				<div class="colonn menuswidth">
					<div>观众服务</div>
					<div class="colonn gyzhview" style="position: absolute;top:0px;width: 7vw;z-index: 99999;">
						<div class="noselmenbrsus">观众服务</div>
						<div class="noselmen"   @click.stop="topage(11)">参观手册</div>
						<div class="noselmen" @click.stop="topage(12)">交通指南</div>
						<div class="noselmen" @click.stop="topage(13)">酒店信息</div>
						<!-- <div class="noselmen" @click.stop="topage(14)">疫情防控</div> -->
					</div>
				</div>
				<div class="colonn menuswidth">
					<div>同期活动</div>
					<div class="colonn gyzhview" 
					style="position: absolute;top:0px;width: 7vw;z-index: 99999;">
						<div class="noselmenbrsus"  >同期活动</div>
						<div class="noselmen"   @click.stop="topage(16)">高峰论坛</div>
						<div class="noselmen"   @click.stop="topage(27)">论坛活动</div>
						
						<!-- <div class="noselmen" @click.stop="topage(17)">专业技术研讨会</div> -->
					</div>
				</div>
				<!-- <div class="colonn menuswidth">
					<div>同期展会</div>
					<div class="colonn gyzhview" style="position: absolute;top:0px;width: 7vw;z-index: 99999;">
						<div class="noselmenbrsus"  >同期展会</div>
						<div class="noselmen"   @click.stop="topage(19)">全屋展</div>
						<div class="noselmen" @click.stop="topage(20)">秋交会</div>
					</div>
				</div> -->

				<div class="colonn menuswidth">
					<div>媒体中心</div>
					<div class="colonn gyzhview" style="position: absolute;top:0px;width: 7vw;z-index: 99999;">
						<div class="noselmenbrsus" >媒体中心</div>
					<!-- 	<div class="noselmen"   @click.stop="topage(22)">新闻中心</div>
						<div class="noselmen" @click.stop="topage(23)">精彩回顾</div> -->
						<div class="noselmen" @click.stop="topage(24)">合作媒体</div>
					</div>
				</div>  
				<div class="colonn menuswidth"  @click.stop="topage(25)">
					<div > 联系我们</div>
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
	.timeivon {
		width: 1.458vw;
		margin-right: 0.742vw;
	}

	.el-dropdown-link {
		font-size: 0.9vw;
	}

	.menuswidth {
		width: 7vw;
		font-size: 1vw;
		position: relative;
	}

	.noselmen {
		background-color: #30913a;
		color: white;
		font-size: 0.93vw;
		padding: 0.3vw 0vw;
	}

	.noselmenbrsus {
		background-color: #30913a;
		color: white;
		font-size: 0.93vw;
		padding: 0.3vw 0vw;
		border-radius: 0.2vw 0.2vw 0vw 0vw;
	}

	.noselmenbrsuslast {
		background-color: #30913a;
		color: white;
		font-size: 0.93vw;
		padding: 0.3vw 0vw;
		border-radius: 0vw 0vw 0.2vw 0.2vw;
	}



	.noselmenbrsus:hover {
		background-color: #ffffff;
		color: #30913a;
		font-size: 0.93vw;
		padding: 0.3vw 0vw;
	}

	.noselmenbrsuslast:hover {
		background-color: #ffffff;
		color: #30913a;
		font-size: 0.93vw;
		padding: 0.3vw 0vw;
	}

	.noselmen:hover {
		background-color: #ffffff;
		color: #30913a;
		font-size: 0.93vw;
		padding: 0.3vw 0vw;
	}
	.gyzhview:hover{
		opacity: 1;
	}
	.gyzhview{
		opacity: 0;
		position: absolute;
	}
</style>