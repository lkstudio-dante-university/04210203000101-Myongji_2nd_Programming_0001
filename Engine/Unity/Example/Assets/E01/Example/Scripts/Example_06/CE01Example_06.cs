#define E06_LIST
#define E06_DICTIONARY
#define E06_STACK_QUEUE

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
 * 컬렉션이란?
 * - 여러 데이터를 저장 및 관리 할 수 있는 기능을 의미한다. (즉, 컬렉션을 활용하면 많은 데이터를 좀 더 효율적으로 제어하는
 * 것이 가능하다는 것을 알 수 있다.)
 * 
 * C# 주요 컬렉션 종류
 * - 리스트
 * - 딕셔너리
 * - 스택/큐
 */
namespace E01 {
	/** Example 6 */
	public partial class CE01Example_06 : CE01SceneManager {
		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_06;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();

#if E06_LIST

#elif E06_DICTIONARY

#elif E06_STACK_QUEUE

#endif // #if E06_LIST
		}
		#endregion // 함수
	}
}
