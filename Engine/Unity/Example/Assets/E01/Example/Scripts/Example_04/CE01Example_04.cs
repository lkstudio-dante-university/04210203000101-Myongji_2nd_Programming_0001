using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
 * 광원이란?
 * - 3 차원 공간에서 물체를 식별 할 수 있게 빛을 발산하는 주체를 의미한다. (즉, 광원은 현실 세계의 태양과 같이 빛을 발사하는
 * 대상이라는 것을 알 수 있다.)
 * 
 * Unity 는 현실 세계에서 물체를 식별하기 위한 원리를 디지털적으로 시뮬레이션하는 엔진이기 때문에 Unity 씬 상에 배치 된
 * 물체를 식별하기 위해서는 반드시 1 개 이상의 광원이 필요하다. (즉, 씬 상에 광원이 존재하지 않을 경우 물체를 식별하는 것이
 * 불가능하다는 것을 알 수 있다.)
 * 
 * Unity 광원 종류
 * - 방향 광원
 * - 포인트 광원
 * - 스포트라이트 광원
 * - 영역 광원 (베이크 전용)
 */
namespace E01 {
	/** Example 4 */
	public partial class CE01Example_04 : CE01SceneManager {
		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_04;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
		}
		#endregion // 함수
	}
}
