using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** 씬 관리자 */
	public abstract partial class CE01SceneManager : CE01Component {
		#region 프로퍼티
		public abstract string SceneName { get; }
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
		}
		#endregion // 함수
	}
}
