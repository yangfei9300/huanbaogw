<template>
	<div>
		<topview></topview>
		<topmenus @myEvent="myEvent"   ></topmenus>
		<!-- 展会概况 -->
		<ab_zhgk v-if="index==0"></ab_zhgk>
		<!-- 展板块 -->
		<ab_zhbk v-if="index==1">></ab_zhbk>
		<!-- 展区分布 -->
		<ab_zqfb v-if="index==2">></ab_zqfb>
		<!-- 组织单位 -->
		<ab_zzdw v-if="index==3">></ab_zzdw>
		<!-- 下载中心 -->
		<ad_xzzx  v-if="index==4">></ad_xzzx>
		
		<!-- 展商服务 -->
		<!-- 为何参展   -->
		<whcz  v-if="index==6"></whcz>
		<!-- 赞助推广 -->
		<zztg v-if="index==7"></zztg>
		<!-- 展商手册完成 -->
		<zssc v-if="index==8"></zssc>
		<!-- 专业观众 -->
		<zygz v-if="index==9"></zygz>
		<!-- 观众服务 -->
		<!-- -->
		<!-- 交通指南 -->
		<jtzn  v-if="index==12"></jtzn>
		<!-- 酒店信息 -->
		<jdxx   v-if="index==13"></jdxx>
		<!-- 同期活动 -->
		<!-- 会议论坛 -->
		<hylt   v-if="index==16"></hylt>
		<!-- 配套活动 -->
		<pthd  v-if="index==17"></pthd>
		<!-- 参观手册 -->
		<cgsc  v-if="index==11"></cgsc>
		
		
		
		
		
		<!-- 联系我们 -->
		<lianxiwomen  v-if="index==25"></lianxiwomen>

		<!-- 媒体中心 xinwenzhongxin -->
		<xinwenzhongxin  v-if="index==22"></xinwenzhongxin>
		<jchg  v-if="index==23"></jchg>
		<hzmt  v-if="index==24"></hzmt>
		<index  v-if="index==26"></index>
		 
		
		<footerview   @myEvent="myEvent" ></footerview>
	</div>
</template>

<script>
	import topview from '../components/topview.vue';
	import footerview from '../components/footer.vue';
	import topmenus from '../components/topmenus.vue';
	import ab_zhgk from '../components/aboutTheExhibition/ab_zhgk.vue';
	import ab_zhbk from '../components/aboutTheExhibition/ab_zhbk.vue';
	import ab_zqfb from '../components/aboutTheExhibition/ab_zqfb.vue';
	import ab_zzdw from '../components/aboutTheExhibition/ab_zzdw.vue';
	import ad_xzzx from '../components/aboutTheExhibition/ad_xzzx.vue';
	import whcz from '../components/zhanshangfuwu/whcz.vue';
	import zztg from '../components/zhanshangfuwu/zztg.vue';
	import zssc from '../components/zhanshangfuwu/zssc.vue';
	import zygz from '../components/zhanshangfuwu/zygz.vue';
	import cgsc from '../components/guanzhongfuwu/cgsc.vue';
	import jtzn from '../components/guanzhongfuwu/jtzn.vue';
	import jdxx from '../components/guanzhongfuwu/jdxx.vue';
	import hylt from '../components/tongqihuodong/hylt.vue';
	import pthd from '../components/tongqihuodong/pthd.vue';
	import lianxiwomen from '../components/lianxiwomen.vue';
	import xinwenzhongxin from '../components/meitizhongxin/xinwenzhongxin.vue';
	import jchg from '../components/meitizhongxin/jchg.vue';
	import hzmt from '../components/meitizhongxin/hzmt.vue';
	import index from '../components/index.vue';


	export default {
		name: 'Home',
		components: {
			topview,
			footerview,
			topmenus,
			ab_zhgk,ab_zhbk,ab_zqfb,ab_zzdw,ad_xzzx,
			whcz,zztg,zssc,
			zygz,cgsc,jtzn,jdxx,hylt,pthd,lianxiwomen,
			xinwenzhongxin,jchg,hzmt,index
		},
		data() {
			return {
				index:26
			}
		},
		created() {
			console.log("asd",this.index)
		},
		methods:{
			myEvent(res){
				console.log("myEvent",res)
				this.index=res.index
			}
		}
	}
</script>

<style>
</style>