using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** UI 빌보드 */
	public class CE01UIsBillboard_23 : CE01Component {
		#region 함수
		/** 상태를 갱신한다 */
		public override void LateUpdate() {
			this.transform.forward = Camera.main.transform.forward;
		}
		#endregion // 함수
	}
}
