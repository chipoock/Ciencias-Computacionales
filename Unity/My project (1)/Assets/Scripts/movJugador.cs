using UnityEngine;

public class movJugador : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created

    public float velocidad = 5f;
    public float rotacion = 120f;
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(KeyCode.A))
        {
            transform.Rotate(0, -rotacion * Time.deltaTime, 0);
        }
        if (Input.GetKey(KeyCode.D))
        {
            transform.Rotate(0, rotacion * Time.deltaTime, 0);

        }
        if (Input.GetKey(KeyCode.W))
        {
            transform.Translate(Vector3.forward * velocidad * Time.deltaTime);
        }
        if (Input.GetKey(KeyCode.S))
        {
            transform.Translate(Vector3.back * velocidad * Time.deltaTime);


        }
    }
}
