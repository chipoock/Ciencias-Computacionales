using UnityEngine;

public class interruptor : MonoBehaviour
{

    public GameObject puente;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnTriggerEnter(Collider other)
    {
        puente.SetActive(true);
        this.gameObject.SetActive(false);
        
    }
}
