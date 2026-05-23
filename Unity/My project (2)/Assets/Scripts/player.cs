using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;

public class NewMonoBehaviourScript : MonoBehaviour
{


    public float velocidad = 5;
    private Rigidbody2D rb;

    public float saltar = 4;

    private bool isGrounded;

    public Transform sueloCheck;

    public float sueloRadius = 0.1f;

    public LayerMask sueloLayer;

    private float mover;


    private int coins;
    public TMP_Text textCoins;


    private Animator animator;
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        animator = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        mover = Input.GetAxisRaw("Horizontal");
        rb.linearVelocity = new Vector2(mover * velocidad, rb.linearVelocity.y);

        if (mover != 0)
        {
            transform.localScale = new Vector3(Mathf.Sign(mover), 1, 1);
        }



        if (Input.GetButtonDown("Jump") && isGrounded)
        {

            rb.linearVelocity = new Vector2(rb.linearVelocity.x, saltar);
        }

        animator.SetFloat("Speed", Mathf.Abs(mover));
        animator.SetFloat("VerticalVelocity", rb.linearVelocity.y);
        animator.SetBool("IsGrounded", isGrounded);

    }



    private void FixedUpdate()
    {
        isGrounded = Physics2D.OverlapCircle(sueloCheck.position, sueloRadius, sueloLayer);
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.transform.CompareTag("Coin"))
        {

            Destroy(collision.gameObject);
            coins++;
            textCoins.text = coins.ToString();
        }


        if (collision.transform.CompareTag("Pinchos"))
        {

            SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        }

        if (collision.transform.CompareTag("Barril"))
        {

            Vector2 knockBackDir = (rb.position - (Vector2)collision.transform.position).normalized;
            rb.linearVelocity = Vector2.zero;
            rb.AddForce(knockBackDir * 9, ForceMode2D.Impulse);

            BoxCollider2D[] colliders = collision.gameObject.GetComponents<BoxCollider2D>();

            foreach (BoxCollider2D col in colliders)
            {
                col.enabled = false;    
            }
            
            collision.GetComponent<Animator>().enabled = true;  
            Destroy(collision.gameObject, 0.5f);

        }
    }
}
