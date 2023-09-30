#define E08_INHERITANCE
#define E08_POLYMORPHISM

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** Example 8 */
	public partial class CE01Example_08 : CE01SceneManager {
		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_08;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
		}
		#endregion // 함수
	}
}
