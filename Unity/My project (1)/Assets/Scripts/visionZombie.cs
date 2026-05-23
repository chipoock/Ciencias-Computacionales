using UnityEngine;
using UnityEngine.UIElements;

public class visionZombie : MonoBehaviour
{
    GameObject jugador;
    private bool activarAnimacion = false;
    Animator animacionZombie;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        jugador = GameObject.Find("jugador");
        animacionZombie = GetComponent<Animator>(); 
    }

    // Update is called once per frame
    void Update()
    {




        if () {
            this.transform.parent.position = Vector3.MoveTowards(this.transform.parent.position,destino,.005f);

            Quaternion rotacionA = this.transform.parent.rotation;
            Quaternion retacionF = Quaternion.LookRotation(destino - transform.parent.position);
            Transform.parent.rotation = Quaternion.RotateTowards();

            animacionZombie.SetBool("corriendo", true);
        }
        else {
            animacionZombie.SetBool("corriendo",false);
            animacionZombie.SetBool("esperando",true);
        
        }
    }
}
