using UnityEngine;

public class personaje : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
         
    }

    public Rigidbody rb;

    // Update is called once per frame
    void Update()
    {
        rb.useGravity = true;
        Debug.Log("Hola Mundo");
        
    }
}
