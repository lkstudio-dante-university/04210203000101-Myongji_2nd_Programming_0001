using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** 싱글턴 */
	public partial class CE01Singleton<T> : CE01Component where T : CE01Singleton<T> {
		#region 클래스 변수
		private static T m_tInst = null;
		#endregion // 클래스 변수

		#region 클래스 프로퍼티
		/*
		 * static 키워드는 해당 멤버가 객체에 종속되는 인스턴스 멤버가 아닌 클래스에 종속되는 정적 멤버라는 것을 알리는
		 * 역할을 수행한다. (즉, 해당 키워드로 명시 된 멤버는 클래스에 종속되기 때문에 객체를 생성하지 않고도 사용하는 것이
		 * 가능하다는 것을 알 수 있다.)
		 */
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

			/*
			 * DontDestroyOnLoad 메서드는 씬이 전환되어도 객체를 제거하지 않도록 설정하는 역할으르 수행한다.
			 * (즉, 일반적으로 Unity 는 씬이 전환되면서 기존 씬이 제거 될 경우 해당 씬 안에 존재하는 모든 게임 객체를
			 * 제거한다는 것을 알 수 있다.)
			 * 
			 * 따라서, 특정 씬 간에 데이터를 공유하고 싶을 경우에는 씬이 전환 되어도 기존 게임 객체가 제거 되지 않도록
			 * 해당 메서드를 이용해야한다. (즉, 해당 메서드의 입력으로 전달 된 게임 객체는 명시적으로 제거하지 않는 이상
			 * 계속 Unity 씬 상에 존재한다는 것을 알 수 있다.)
			 */
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
