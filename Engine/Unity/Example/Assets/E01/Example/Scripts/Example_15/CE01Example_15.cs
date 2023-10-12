#define E15_SPRITE
#define E15_ANIMATION

#if E15_ANIMATION
#define E15_ANIMATION_TWEEN
#define E15_ANIMATION_KEY_FRAME
#endif // #if E15_ANIMATION

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** Example 15 */
	public partial class CE01Example_15 : CE01SceneManager {
		#region 변수
		[SerializeField] private SpriteRenderer m_oSprite = null;
		#endregion // 변수

		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_15;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
		}
		#endregion // 함수
	}
}
