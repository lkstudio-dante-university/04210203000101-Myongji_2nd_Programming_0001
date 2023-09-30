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
			SceneManager.LoadScene(a_oName, a_bIsSingle ? LoadSceneMode.Single : LoadSceneMode.Additive);
		}

		/** 씬을 비동기 로드한다 */
		public void LoadSceneAsync(string a_oName, System.Action<CE01SceneLoader, AsyncOperation, bool> a_oCallback, bool a_bIsSingle = true) {
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
				yield return null;
				a_oCallback?.Invoke(this, oAsyncOperation, false);
			} while(oAsyncOperation.isDone);

			a_oCallback?.Invoke(this, oAsyncOperation, true);
		}
		#endregion // 함수
	}
}
