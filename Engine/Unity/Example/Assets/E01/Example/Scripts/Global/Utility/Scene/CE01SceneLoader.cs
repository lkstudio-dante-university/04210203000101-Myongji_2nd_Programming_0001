using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace E01 {
	/** 씬 로더 */
	public partial class CE01SceneLoader : CE01Singleton<CE01SceneLoader> {
		#region 함수
		/** 씬을 로드한다 */
		public void LoadScene(string a_oName, bool a_bIsSingle = true) {
			/*
			 * SceneManager 클래스란?
			 * - 씬을 제어 할 수 있는 여러 기능을 지원하는 클래스를 의미한다. (즉, 해당 클래스를 활용하면 프로그램이 실행
			 * 중에 다른 씬으로 전환하는 것이 가능하다.)
			 * 
			 * Unity 씬 로드 방식 종류
			 * - Single
			 * - Additive
			 * 
			 * Single vs Additive
			 * - Single 로드 방식은 기존에 로드 되어있는 모든 씬을 제거하고 새로운 씬을 로드하는 특징이 존재한다. (즉, 해당
			 * 방식으로 씬을 로드하면 기존에 존재하는 모든 씬이 제거된다는 것을 알 수 있다.)
			 * 
			 * 반면, Additive 로드 방식은 기존에 존재하는 씬은 그대로 두고 새로운 씬을 중첩으로 로드하는 차이점이 존재한다.
			 * (즉, Additive 로드 방식은 여러 씬을 로드 할 때 사용하는 방식이라는 것을 알 수 있다.)
			 */
			SceneManager.LoadScene(a_oName, a_bIsSingle ? LoadSceneMode.Single : LoadSceneMode.Additive);
		}

		/** 씬을 비동기 로드한다 */
		public void LoadSceneAsync(string a_oName, System.Action<CE01SceneLoader, AsyncOperation, bool> a_oCallback, bool a_bIsSingle = true) {
			/*
			 * StartCoroutine 메서드는 코루틴을 시작하는 역할을 수행한다. (즉, 해당 메서드를 활용하면 여러 작업을 병렬적으로 
			 * 처리하는 것이 가능하다는 것을 알 수 있다.)
			 * 
			 * 코루틴이란?
			 * - 일반적인 메서드와 달리 메서드 호출이 종료된 위치부터 다시 이어서 실행 할 수 있는 메서드를 의미한다. (즉,
			 * 일반적인 메서드는 호출이 종료되고 나면 다시 처음부터 호출되는 특징이 존재하며 이러한 메서드를 서브루틴이라고
			 * 한다.)
			 * 
			 * 따라서, 코루틴을 활용하면 여러 작업을 병렬적으로 처리하는 병렬 처리 구조를 만들어내는 것이 가능하다.
			 */
			StartCoroutine(this.CoLoadSceneAsync(a_oName, a_oCallback, a_bIsSingle));
		}
		#endregion // 함수
	}

	/** 씬 로더 - 코루틴 */
	public partial class CE01SceneLoader : CE01Singleton<CE01SceneLoader> {
		#region 함수
		/** 씬을 비동기 로드한다 */
		private IEnumerator CoLoadSceneAsync(string a_oName, System.Action<CE01SceneLoader, AsyncOperation, bool> a_oCallback, bool a_bIsSingle) {
			var oAsyncOperation = SceneManager.LoadSceneAsync(a_oName, a_bIsSingle ? LoadSceneMode.Single : LoadSceneMode.Additive);

			do {
				/*
				 * yield return 키워드란?
				 * - 코루틴에서만 사용 가능한 키워드로서 해당 키워드를 명시하면 코루틴을 종료하고 흐름을 해당 메서드를 호출
				 * 한 곳으로 되돌리는 역할을 수행한다. (즉, return 키워드와 비슷한 역할이라는 것을 알 수 있다.)
				 * 
				 * 단, 코루틴은 반드시 IEnumerator 인터페이스를 따르는 객체를 반환해야되기 때문에 일반적인 메서드와 달리
				 * 항상 반환 값이 존재한다는 특징이 있다. (즉, 코루틴 내부에서는 해당 키워드를 반드시 1 번 이상 명시해야되는
				 * 것을 알 수 있다.)
				 * 
				 * 만약, 코루틴에서 적절한 반환 값이 없을 경우에는 null 값을 반환하면 된다.
				 */
				yield return null;
				a_oCallback?.Invoke(this, oAsyncOperation, false);
			} while(oAsyncOperation.isDone);

			a_oCallback?.Invoke(this, oAsyncOperation, true);
		}
		#endregion // 함수
	}
}
