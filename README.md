## Feature 0: Emoji and Media Handling
1. Emojis, if any, on senders name will be removed

2. Emojis will be replaced with their corresponding `CLDR Short Name` representations.

3. Any other, non emoji and non ascii character, will be replaced by a similar
  combination of ascii characters. If not possible, replace with it with '@'.
  If multiple non-asccii characters in sequence, replace them with "n@", being
  'n' the number of non-ascii characters found.

4. Media files will be omitted from the conversation, and "<Media omitted>" will
  be displayed instead. If more than one "<Media ommitted>" are found in a row,
  they will be replaced by "<n Media ommited>", being 'n' the number of
  occurrences

```txt
4/23/23, 11:01 PM - Alberto Rodriguez: Mucha metafora
4/23/23, 11:20 PM - Danyiel Colin 🤖: <Media omitted>
4/23/23, 11:25 PM - Danyiel Colin 🤖: <Media omitted>
4/23/23, 11:25 PM - Alberto Rodriguez: Y eso?
4/23/23, 11:25 PM - Danyiel Colin 🤖: En la mañana jugué basket con Mateo 😀
4/23/23, 11:26 PM - Danyiel Colin 🤖: <Media omitted>
4/23/23, 11:27 PM - Danyiel Colin 🤖: <Media omitted>
4/23/23, 11:27 PM - Danyiel Colin 🤖: <Media omitted>
4/23/23, 11:28 PM - Danyiel Colin 🤖: Ya luego recuperaré el glamour
4/23/23, 11:28 PM - Alberto Rodriguez: Auch 😬
4/23/23, 11:28 PM - Danyiel Colin 🤖: Por eso creo que َ∓1
```

```markdown
4/23/23, 11:01 PM - Alberto Rodriguez: Mucha metafora

4/23/23, 11:20 PM - Danyiel Colin: <2 Media omitted>

4/23/23, 11:25 PM - Alberto Rodriguez: Y eso?

4/23/23, 11:25 PM - Danyiel Colin: En la mañana jugué basket con Mateo :grinning face:
4/23/23, 11:26 PM - Danyiel Colin: <3 Media omitted>
4/23/23, 11:28 PM - Danyiel Colin: Ya luego recuperaré el glamour

4/23/23, 11:28 PM - Alberto Rodriguez: Auch :grimacing face:

4/23/23, 11:28 PM - Danyiel Colin 🤖: Por eso creo que -+1
```


## Feature 1: Date and Heading Handling

1. A heading with the date will be added at the top of each day's conversation.

2. If the date changes within the conversation, a new heading using a level 2
  heading format (##) will be added to indicate the new date. But if there are
  messages in a row from the same sender, even if the differ at some point,
  they will be kept on the conversation of first date.

3. The date and hour will be removed from the line

```txt
4/23/23, 11:33 PM - Alberto Rodriguez: Jjaj
4/23/23, 11:33 PM - Alberto Rodriguez: Auchh
4/23/23, 11:33 PM - Alberto Rodriguez: Y duele?
4/23/23, 11:34 PM - Danyiel Colin: Intentar giñar ese ojo o acostarme con ese lado en la almohada, sí
4/24/23, 00:04 PM - Danyiel Colin: Pero si estoy tranqui, no
4/24/23, 00:15 PM - Alberto Rodriguez: Entiendo
4/24/23, 00:15 PM - Alberto Rodriguez: Auch
4/24/23, 00:16 PM - Alberto Rodriguez: Que bueno que no sea tan malo
```

```markdown
## 4/23/23
-- Alberto Rodriguez: Jjaj
-- Alberto Rodriguez: Auchh
-- Alberto Rodriguez: Y duele?
-- Danyiel Colin: Intentar giñar ese ojo o acostarme con ese lado en la almohada, sí
-- Danyiel Colin: Pero si estoy tranqui, no

## 4/24/23
-- Alberto Rodriguez: Entiendo
-- Alberto Rodriguez: Auch
-- Alberto Rodriguez: Que bueno que no sea tan malo
```

## Feature 2: Message Formatting and Grouping

1. Messages from the same sender that appear consecutively will be merged into a
  single block, separated by a punctuation mark (period, comma or question mark).

2. Each merged block of messages from the same sender will be preceded by the
  sender's name.

3. Line breaks will be added after each merged block to improve clarity and
  separation.

4. List syntax (-, a. 1.) will be kept, and break lines below and over will be
  added

```txt
4/23/23, 7:49 PM - Danyiel Colin: Reversible virtualmente puesto que a efectos prácticos, no se nota en la parte central. Lo virtual es porque se admite la posible modificación indeleble de algún componente no visible
4/23/23, 7:49 PM - Danyiel Colin: Así es
4/23/23, 7:49 PM - Alberto Rodriguez: No hay nada malo en lo que haces mientras eres diferente?
4/23/23, 7:50 PM - Alberto Rodriguez: Ya veo
4/23/23, 7:50 PM - Danyiel Colin: No hay nada de malo dado que no es permanente
4/23/23, 7:50 PM - Alberto Rodriguez: En tu mente lo es
4/23/23, 7:50 PM - Danyiel Colin: Lo que es permanente es mi posibilidad para cambiar otra vez al nuevo estado hallado. No es permanente que me quede en ese estado
4/23/23, 7:50 PM - Danyiel Colin: De ahí lo virtual
4/23/23, 7:53 PM - Danyiel Colin: De hecho, dado que tiene 3 miembros la fórmula, hay 4 subconjuntos de igualdad. Que combinados con la discretizacion del rango moral de *p* (la acción) en _Bueno, Malo, Neutro_, nos da un esquema de 12 casos base a analizar.
4/23/23, 7:58 PM - Danyiel Colin: Calculé mal el conjunto potencia. Son 5 de hecho. Analizando solo los subconjuntos respecto la igualdad:
- (altruista) a = x
- (egoísta) a = y
- (dominación) x = y
- (pragmático) x ≠ y
- (autonomía) a = x = y
4/23/23, 7:49 PM - Danyiel Colin: Así es
4/23/23, 7:49 PM - Alberto Rodriguez: Ya veo
```

```markdown
-- Danyiel Colin: Reversible virtualmente puesto que a efectos prácticos, no se
nota en la parte central. Lo virtual es porque se admite la posible
modificación indeleble de algún componente no visible. Así es

-- Alberto Rodriguez: No hay nada malo en lo que haces mientras eres diferente? Ya veo

-- Danyiel Colin: No hay nada de malo dado que no es permanente

-- Alberto Rodriguez: En tu mente lo es

-- Danyiel Colin: Lo que es permanente es mi posibilidad para cambiar otra vez
al nuevo estado hallado. No es permanente que me quede en ese estado. De ahí lo
virtual. De hecho, dado que tiene 3 miembros la fórmula, hay 4 subconjuntos de
igualdad. Que combinados con la discretizacion del rango moral de *p* (la
acción) en _Bueno, Malo, Neutro_, nos da un esquema de 12 casos base a
analizar. Calculé mal el conjunto potencia. Son 5 de hecho. Analizando solo los
subconjuntos respecto la igualdad:

- (altruista) a = x
- (egoísta) a = y
- (dominación) x = y
- (pragmático) x ≠ y
- (autonomía) a = x = y

Así es

-- Alberto Rodriguez: Ya veo
```

## Example implementing all features
`action-f0.2` is a comment meaning `action by feature 0, section 2`. It's not meant to be on
the final output, just to clarification purposes

```txt
5/26/22, 2:52 AM - Danyiel Colin: Mmm, voto por Valentina
5/26/22, 2:52 AM - Danyiel Colin: Abigail también se quiere especializar en oncología
5/26/22, 2:53 AM - Alberto Rodriguez 👾: 😮
5/26/22, 2:54 AM - Danyiel Colin: Así que ya visualizo el plan
5/26/22, 2:54 AM - Danyiel Colin: <Media ommited>
5/26/22, 2:54 AM - Danyiel Colin: <Media ommited>
5/26/22, 2:54 AM - Danyiel Colin: <Media ommited>
5/26/22, 2:54 AM - Alberto Rodriguez 👾: Siempre visualizando tú
5/26/22, 2:54 AM - Alberto Rodriguez 👾: No sé
5/26/22, 2:54 AM - Danyiel Colin: Todo puede tener un propósito
5/26/22, 2:54 AM - Alberto Rodriguez 👾: Mi corazón no quiere a ninguna
5/26/22, 2:55 AM - Alberto Rodriguez 👾: No tengo un fuerte sentimiento por ninguna
5/26/22, 2:55 AM - Danyiel Colin: Mejor, puedes tomar decisiones basadas en la razón
5/26/22, 2:55 AM - Alberto Rodriguez 👾: Solo puedo decir que me caen bien y les tengo cariño
5/27/22, 2:55 AM - Alberto Rodriguez 👾: Son buenas mujeres
5/27/22, 2:55 AM - Alberto Rodriguez 👾: Pero hoy Valentina me hizo ver que sí quiere algo
5/27/22, 2:55 AM - Danyiel Colin: Estar enamorado es en cierto modo frívolo. Muchos recursos consumidos
5/27/22, 2:55 AM - Alberto Rodriguez 👾: Entendiste lo que dije?
5/27/22, 2:55 AM - Alberto Rodriguez 👾: Kkkk
5/27/22, 2:55 AM - Danyiel Colin: Sí
5/27/22, 2:56 AM - Danyiel Colin: Sí entendi
5/27/22, 2:56 AM - Alberto Rodriguez 👾: 1. Valentina me miraba al reírse
5/27/22, 2:56 AM - Alberto Rodriguez 👾: 2. Me aceptó en corto a salir
5/27/22, 2:56 AM - Alberto Rodriguez 👾: Nos despedimos hoy en persona del alemán, todo normal
```

```markdown
## 5/26/22

-- Danyiel Colin: Mmm, voto por Valentina. Abigail también se quiere
especializar en oncología

-- Alberto Rodriguez: :face with open mouth:

-- Danyiel Colin: Así que ya visualizo el plan <3 Media ommitted>

-- Alberto Rodriguez: Siempre visualizando tú. No sé

-- Danyiel Colin: Todo puede tener un propósito

-- Alberto Rodriguez: Mi corazón no quiere a ninguna. No tengo un fuerte
sentimiento por ninguna

-- Danyiel Colin: Mejor, puedes tomar decisiones basadas en la razón

-- Alberto Rodriguez: Solo puedo decir que me caen bien y les
tengo cariño. Son buenas mujeres. Pero hoy Valentina me hizo ver que sí quiere
algo

## 5/27/22

-- Danyiel Colin: Estar enamorado es en cierto modo frívolo. Muchos recursos consumidos

-- Alberto Rodriguez: Entendiste lo que dije?. Kkkk

-- Danyiel Colin: Sí. Sí entendi

-- Alberto Rodriguez: 

1. Valentina me miraba al reírse
2. Me aceptó en corto a salir

Nos despedimos hoy en persona del alemán, todo normal
```
