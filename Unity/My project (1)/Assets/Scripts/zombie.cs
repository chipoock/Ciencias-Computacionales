using UnityEngine;

public class zombie : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    Animator AniZombie;
    void Start()
    {
        AniZombie = transform.GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.name = "pelota(clone)") {
            AniZombie.SetBool("muerte",true);
            Destroy(this.gameObject,3.0f);
            //Transform vision = this.transform.Find("zombieVision");
            //vision.parent = null;
        
        }
    }
}
