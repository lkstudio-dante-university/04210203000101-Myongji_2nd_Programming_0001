using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** 싱글턴 */
	public class CE01Singleton<T> : CE01Component where T : CE01Singleton<T> {
		#region 클래스 변수
		private static T m_tInst = null;
		#endregion // 클래스 변수

		#region 클래스 프로퍼티
		public static T Inst {
			get {
				// 인스턴스가 없을 경우
				if(CE01Singleton<T>.m_tInst == null) {
					var oGameObj = new GameObject(typeof(T).ToString());
					CE01Singleton<T>.m_tInst = oGameObj.AddComponent<T>();
				}

				return CE01Singleton<T>.m_tInst;
			}
		}
		#endregion // 클래스 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
			CE01Singleton<T>.m_tInst = this as T;

			DontDestroyOnLoad(CE01Singleton<T>.m_tInst.gameObject);
		}
		#endregion // 함수

		#region 클래스 함수
		/** 인스턴스를 생성한다 */
		public static T Create() {
			return CE01Singleton<T>.m_tInst;
		}
		#endregion // 클래스 함수
	}
}
