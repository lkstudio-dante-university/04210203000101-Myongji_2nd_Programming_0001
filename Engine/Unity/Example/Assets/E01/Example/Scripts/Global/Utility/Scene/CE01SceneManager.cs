using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace E01 {
	/** 씬 관리자 */
	public abstract partial class CE01SceneManager : CE01Component {
		#region 프로퍼티
		public abstract string SceneName { get; }

		public GameObject UIs { get; private set; } = null;
		public GameObject PopupUIs { get; private set; } = null;

		public GameObject Objs { get; private set; } = null;
		public GameObject StaticObjs { get; private set; } = null;

		public bool IsActiveScene => SceneManager.GetActiveScene().name.Equals(this.SceneName);
		public bool IsAdditiveScene => !this.IsActiveScene;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
			this.SetupDefObjs();

			Physics.gravity = KE01Define.G_PHYSICS_GRAVITY;
			Application.targetFrameRate = Mathf.RoundToInt((float)Screen.currentResolution.refreshRateRatio.value);
		}

		/** 상태를 갱신한다 */
		public override void Update() {
			base.Update();

			// 뒤로가기 키를 눌렀을 경우
			if(Input.GetKeyDown(KeyCode.Escape) && !this.SceneName.Equals(KE01Define.G_SCENE_N_EXAMPLE_00)) {
				CE01SceneLoader.Inst.LoadScene(KE01Define.G_SCENE_N_EXAMPLE_00);
			}
		}

		/** 기본 객체를 설정한다 */
		private void SetupDefObjs() {
			var oGameObjList = new List<GameObject>();
			this.gameObject.scene.GetRootGameObjects(oGameObjList);

			for(int i = 0; i < oGameObjList.Count; ++i) {
				/*
				 * Transform 컴포넌트의 Find 메서드를 활용하면 특정 게임 객체의 자식 객체를 탐색하는 것이 가능하다. 
				 * 또한, 해당 메서드는 경로를 지정함으로서 자식 객체 뿐만 아니라 후손 객체도 탐색 할 수 있는 특징이 존재한다.
				 */
				var oUIs = oGameObjList[i].transform.Find("Canvas/UIs")?.gameObject;
				var oPopupUIs = oGameObjList[i].transform.Find("Canvas/PopupUIs")?.gameObject;

				var oObjs = oGameObjList[i].transform.Find("Objs")?.gameObject;
				var oStaticObjs = oGameObjList[i].transform.Find("StaticObjs")?.gameObject;

				this.UIs = this.UIs ?? oUIs;
				this.PopupUIs = this.PopupUIs ?? oPopupUIs;

				this.Objs = this.Objs ?? oObjs;
				this.StaticObjs = this.StaticObjs ?? oStaticObjs;
			}
		}
		#endregion // 함수
	}
}
