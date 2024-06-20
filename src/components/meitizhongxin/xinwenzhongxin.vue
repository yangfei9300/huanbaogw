<template>
	<div class="colonn">
		<img src="https://xintfboys.mianshijing.top/img/banner_3.fa38cdc3.jpg" style="width: 100vw;">
		<div class="breadcrumb roww center_center"><img
				src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAqVJREFUSEvNlMtrE2EUxc/5ZpK0lEYUrYjbbkxDkkkiLnRRRGkLCoorV8W14sqViFRa33YhhQoGdSOCCxeu/CPKdJISrY8K9YFQKWpiH6TpzJUvJGFo0yahGwdmM9z7m8O95x6ihae3tzfU1dUVNwzj7/T09AcAXrM2NisAoCzLOkLyNoCC67pXc7nc22Z9zcAqnU6nPc+7T/IoABfA6/X19Wu5XO7jdvDtwEwmk0kA4ySPATA0SERKJF8BuG7b9uet4FuBGY/HE6Zp3gVwvAb1QVYBvHRd90Y2m51vBG8EZiKR0IuqQc1GjSKyDOC5YRg3p6amvm2s2QhmOp3uq870BICGUB+kKCLPROSe4zg//HA/mLFYrM80zVskBwEEmm2+OvM/ADJra2vj+Xx+odZTB1uWFdGWIjnUKtT3418AJgE8tG17UX9nKpUKiMghAGMkBwAEW1G6sUZEfpOcKJfLmZmZme96+wcDgcAVz/POANilX5KqTXgZwKKI/CT5xLbtCUYikWAoFDoAYB/JsyQvAQi3AxaRec/zLiqlFkRk1XGcd/UZ9/f3m0tLS8N6wwD2VBcjJFe0tUjW8sEQkTBJPbJa/2ypVBrI5/N129XBWnlHR8cwyTs+sL6yNwBekFx2XVeUUrsBXBaRw76RzQIYtG376yZX6AQLh8MarMOmohjACoBHruuOZbPZgv4QjUZ7gsHgYwCnfOD3AAbaAovIZLFYHJ2bmytqsGVZ+5RSGRE5vSOwVgxg1LbtiuJYLNZjmmZmx4r/b3B3d/cFpZR2hT6USvZqxSRHaqOIRqP7Q6HQUxEZIllxlYh8EpGTjuN82eQKbbfOzs7zAEaqrhAAOnczhULhQW15qVRqr84Eba9qTusrnS2Xy+f0KW8Ct3NprdT+A4i2NyYPIiAgAAAAAElFTkSuQmCC"
				alt="" style="margin-right:10px;">
			<div>首页 — 媒体中心 — 新闻中心 </div>
			<div class="allline"></div>
		</div>
		<div data-v-6159cbc4="" id="com-title">
			<div>新闻中心</div>
		</div>


		<div id="media-news" style="text-align: left;">
			<ul class="tab" style="padding-left: 0px;">
				<li 
				 :class="{
					 'active':typeIndex==1,
				 }"
				 
				 @click="typeIndexClick(1)"> 展会新闻 </li>
				<li 
				 :class="{
					 'active':typeIndex==2,
				 }"
				   @click="typeIndexClick(2)"> 展会快讯 </li>
				<li 
				 :class="{
					 'active':typeIndex==3,
				 }"
				   @click="typeIndexClick(3)"> 行业资讯 </li>
			</ul>
			<section v-if="typeIndex==1">
				
					<div>
						
						<div>
							<div class="roww rowsb">
								<video v-for="(item,index) in 4"
									src="https://upload.zhongsheyun.com/5iDwTj4QTjH3UU9hi6JI9S/1673512329713282.mp4" controls
									class="video11"></video>
							</div>
						
						<ul class="news-l" style="padding-left: 0px;">
							<li>
								<div class="text">澎湃新闻 | 定了！永久会址落户合肥</div>
								<div class="time"> 2023-08-15 </div>
							</li>
							<li>
								<div class="text">人民网 | 2021中国污染防治联展在合肥举行</div>
								<div class="time"> 2022-04-12 </div>
							</li>
							<li>
								<div class="text">潇湘晨报 | 聚焦碳达峰碳中和推动生态文明建设——2021中国污染防治联展在合肥举行</div>
								<div class="time"> 2022-04-12 </div>
							</li>
							<li>
								<div class="text">凤凰网 | 2021中国防污联展“科技助力深入打好污染防治攻坚战”</div>
								<div class="time"> 2022-04-12 </div>
							</li>
							<li>
								<div class="text">科技智囊 | 创新赋能&nbsp;科技增效|启迪环境无人环卫“黑科技”吸睛污防展</div>
								<div class="time"> 2022-04-12 </div>
							</li>
							<li>
								<div class="text">新浪网安徽 | “中国环境谷”惊艳亮相2021中国污染防治联展</div>
								<div class="time"> 2022-04-12 </div>
							</li>
							<li>
								<div class="text">安徽新闻网 | 探秘水陆空治污“神器”</div>
								<div class="time"> 2022-04-12 </div>
							</li>
							<li>
								<div class="text">安徽环境新闻网 | “2021中国污染防治联展”在安徽合肥圆满落幕</div>
								<div class="time"> 2022-04-12 </div>
							</li>
							<li>
								<div class="text">凤凰网 | “中国环境谷”惊艳亮相2021中国污染防治联展！</div>
								<div class="time"> 2022-04-12 </div>
							</li>
							<li>
								<div class="text">网易 | 2021年中国污染防治联展合肥市王民生副市长巡展</div>
								<div class="time"> 2022-04-12 </div>
							</li>
						</ul>
					</div>
					
				</div>
			</section>
			
			
			
			<section  v-if="typeIndex==2" >
				<div>
					<ul class="news-list">
						<li>
							<div class="time"><span>05</span> 2023-07 </div>
							<div class="text">展会开幕在即！这份参观指南请收好→</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>05</span> 2023-07 </div>
							<div class="text">新环会最新参展指南！报道、布展、住宿等全流程要点，请收藏！</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>01</span> 2023-06 </div>
							<div class="text">凯华环保：解决工厂的排污之忧，重现失去的碧水蓝天！</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>01</span> 2023-06 </div>
							<div class="text">打造新能源和节能环保产业万亿俱乐部，安徽有啥优势？</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>01</span> 2023-06 </div>
							<div class="text">120亿！安徽省新能源和节能环保产业基金落户蜀山经开区！</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>01</span> 2023-06 </div>
							<div class="text">中国新环会第四批专业观众名单公布！</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>01</span> 2023-06 </div>
							<div class="text">走访记实 | 中国新环会组委会赴“城市管理技术与装备博览会”考察交流！</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>01</span> 2023-06 </div>
							<div class="text">中华环保联合会关于邀请参加第二届中国新环会的通知（第一轮）</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>01</span> 2023-06 </div>
							<div class="text">新环会广告赞助 | 全方位宣传，立体式呈现，多维度回报！</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>01</span> 2023-06 </div>
							<div class="text">新环会系列活动—河湖生境改善与生态恢复主题论坛</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
					</ul>
					
				</div>
			</section>
			<section  v-if="typeIndex==3" >
				<div>
					<ul class="news-list">
						<li>
							<div class="time"><span>26</span> 2021-10 </div>
							<div class="text">安徽省巢湖管理局 | 习近平在深入推动黄河流域生态保护和高质量发展座谈会上强调
								咬定目标脚踏实地埋头苦干久久为功 为黄河永远造福中华民族而不懈奋斗 韩正出席并讲话</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>22</span> 2021-10 </div>
							<div class="text">合肥高新技术产业开发区管理委员会</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>22</span> 2021-10 </div>
							<div class="text">安徽省生态环境厅</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>22</span> 2021-10 </div>
							<div class="text">中国环境网</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>22</span> 2021-10 </div>
							<div class="text">中国环境网</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>22</span> 2021-10 </div>
							<div class="text">中国环境网</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>22</span> 2021-10 </div>
							<div class="text">中国环境报社</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>22</span> 2021-10 </div>
							<div class="text">中华环保联合会</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>23</span> 2021-07 </div>
							<div class="text">第一环保网</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
						<li>
							<div class="time"><span>23</span> 2021-07 </div>
							<div class="text">第一环保网</div><img
								src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAl5JREFUWEfN2M9rE0EUwPHvmyYNIm1zsBhS449r9aS5FD14UBDEEpTcW81fIE2reBFEij15sf+Axyoe9NCL4EFFoSCI9SaKBhSrFyGCptmRTY2GYnZnksyse92Znc+8N7PzdoX//BJrX/lzjmZ9P43MS+7nv1v3t+xgB5x+nyct8whTaL3I18IDHsmm5ZhWzc2BLRxzCBfQMgKsI3KZLxOrLpFmwL+48yBjWyGQAB28RpRTZAzwquJsJY8EFxE6cO0suUdGA8sfxwkalxCpAKP/XjxukdHAM+8OkBm6AZSAdPfV7Q4ZDTyylmZvbhIVXEM4BeIdabBJtHDu0yQ0FpNAGgDDxCaHNAQmh7QAJoO0BPpH9gD0i+wR6A/ZB9APsk+ge+QAgB1I2byO5iTCjrDciTy7NVfYOfyQ27l6VIE4IOBvZLl2iIBbwDGkG7BdqulXBCxwr7DqC6go1YqkWAYOd49gi9ME/RQtVe4WnnsAakW5VkQTVj5TQCZi0CbwGM0C6tsLVg7+dAz8g1tqpRaGYnHCPCt71lpVeczV5xp0i2ut1rgZdL/vHtcH0A+uR6A/XA9AvzhLoH+cBTAZnCEwOVw8sLw+jM4W0UH4RXd00C9hk1ecwYd76ibo00ng4iM4vTFC+kcF0XNAvsuMt85Wi+PLJHLtNvEnSeltFqVmUCpETmx7uFNcfATbmhNvxhhNzW5DOseZA8OWITKbmYWgCrIbzRMUVdOqxCatnW3jU9zZOkx3Kj0D+jioJe7kn5mUTL3i7CLYHiXcOJn6Ljb2fXD569d8k/Qz/QH0/QU8T3M4jPgCZwAAAABJRU5ErkJggg=="
								alt="">
						</li>
					</ul>
					
				</div>
			</section>
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
				typeIndex:1
			}
		},
		beforeMount() {
		},
		beforeDestroy() {
			
		},
		mounted() {
		
		},
		methods: {
			typeIndexClick(index){
				this.typeIndex=index;
			}
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
li{list-style-type:none;}
	#overview {
		margin: 0 18.75vw;
		margin-bottom: 2.604vw;
		border: 1px solid #b5b2b2;

		padding: 3.125vw 3.646vw;
		text-align: left;
	}



	.video-list .video-li {
		width: 13.854vw;
		position: relative
	}

	.video-list .video-li .img-box {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		left: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		pointer-events: none;
		z-index: 1
	}

	.video-list .video-li .img-box img {
		width: 2.552vw;
		pointer-events: none
	}

	.video-list .video-li .foot {
		font-size: .833vw;
		margin-top: 1.042vw
	}

	.video-list .video-li .foot p {
		margin-bottom: .521vw
	}

	.video-list .video-li .foot span {
		color: grey
	}

	.video-list {
		display: flex;
		justify-content: space-between;
		flex-wrap: wrap;
		padding-bottom: 1.042vw;
		margin-bottom: 1.563vw;
		border-bottom: 1px solid #b5b2b2
	}

	.video-list .video-js {
		width: 100%;
		height: 8.542vw
	}

	.video-list .vjs-big-play-button {
		display: none
	}

	.video-list .img-box {
		height: 8.542vw
	}

	.video-list .video-item {
		width: 100%;
		height: 7.813vw;
		display: flex
	}

	.news-l li {
		font-size: .938vw;
		color: #333;
		border-bottom: 1px solid #b5b2b2;
		line-height: 3.125vw;
		display: flex;
		justify-content: space-between;
		padding: 0 3.125vw
	}

	.news-l li .time {
		color: grey
	}

	.pagination {
		text-align: center;
		margin-top: 1.823vw
	}

	.warp {
		width: 100%;
		height: 15.104vw;
		overflow: hidden;
		flex: auto
	}

	.warp .scroll-warp {
		display: flex;
		justify-content: space-between;
		line-height: 2.604vw;
		cursor: pointer
	}

	.pagination[data-v-a1178786] {
		text-align: center;
		margin-top: 1.823vw
	}

	#media-brief ul li[data-v-040b82cf] {
		display: flex;
		justify-content: space-between;
		align-items: center;
		border-bottom: 1px solid #b5b2b2;
		padding: 1.563vw 0
	}

	#media-brief ul li img[data-v-040b82cf] {
		width: 7.292vw;
		height: 7.292vw
	}

	#media-brief ul li .text-box[data-v-040b82cf] {
		flex: 5;
		padding-left: 3.646vw
	}

	#media-brief ul li .text-box h4[data-v-040b82cf] {
		font-size: 1.042vw;
		font-weight: 600
	}

	#media-brief ul li .text-box p[data-v-040b82cf] {
		line-height: 1.354vw
	}

	#media-brief ul li .time[data-v-040b82cf] {
		flex: 1;
		font-size: 1.042vw
	}

	#media-brief .pagination[data-v-040b82cf] {
		text-align: center;
		margin-top: 1.823vw
	}

	#media-news {
		margin: 0 18.75vw;
		margin-bottom: 2.604vw;
		border: 1px solid #b5b2b2;
		padding: 2.604vw
	}

	#media-news .tab {
		display: flex;
		margin-bottom: 2.083vw
	}

	#media-news .tab li {
		width: 50%;
		border: 1px solid #b5b2b2;
		text-align: center;
		line-height: 3.646vw;
		font-size: 1.458vw;
		cursor: pointer
	}

	#media-news .tab li:first-child {
		border-right: unset
	}

	#media-news .tab li:last-child {
		border-left: unset
	}

	#media-news .news-list li {
		padding: 1.563vw 1.042vw;
		border-bottom: 1px solid #b5b2b2;
		display: flex;
		justify-content: space-between;
		align-items: center;
		cursor: pointer
	}

	#media-news .news-list li .time {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		width: 4.375vw;
		height: 4.375vw;
		border: 1px solid #333;
		font-size: .833vw;
		flex: 1
	}

	#media-news .news-list li .time span {
		font-weight: 600;
		font-size: 2.083vw
	}

	#media-news .news-list li .text {
		flex: 10;
		margin-left: 2.083vw;
		font-size: .938vw
	}

	#media-news .news-list li img {
		width: 2.083vw;
		height: 2.083vw
	}

	#media-news .active {
		color: #fff;
		background: #0054e0
	}
	.video11 {
		height: 7vw;
	}
</style>